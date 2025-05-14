import json
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.types import ASGIApp
from fastapi import FastAPI  # 用于类型提示和应用示例
from fastapi.exceptions import HTTPException  # 用于检查 FastAPI 的异常类型


class UnifiedJsonResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # 调用链中的下一个处理器（可能是另一个中间件或路由处理函数）
        response = await call_next(request)

        # 仅当响应的媒体类型是 "application/json" 时才进行处理
        if response.media_type == "application/json":
            # 读取原始响应体
            # 这会消耗 response.body_iterator，所以我们之后必须返回一个新的响应对象
            response_body_bytes = b""
            async for chunk in response.body_iterator:
                response_body_bytes += chunk

            original_data = None  # 用于存储解析后的原始 JSON 数据
            # is_valid_json_payload = False # 标记原始负载是否为有效JSON，这里暂时不用

            if response_body_bytes:  # 如果响应体不为空
                try:
                    # 解码字节串并解析原始 JSON 数据
                    # response.charset 通常是 'utf-8'
                    original_data = json.loads(
                        response_body_bytes.decode(response.charset or "utf-8")
                    )
                    # is_valid_json_payload = True
                except json.JSONDecodeError:
                    # 这意味着上游处理器设置了 media_type="application/json"
                    # 但发送了格式错误的 JSON。我们应该指示一个错误。
                    # 目前，我们将让 original_data 保持为 None，并且 message 会反映错误。
                    # 更健壮的解决方案可能是在这里返回一个 500 错误。
                    print(f"警告: 来自 {request.url.path} 的上游响应包含格式错误的JSON")
                    # 简单起见，original_data 保持为 None，message 字段将指示错误。
                    pass  # original_data 保持为 None

            # 确定统一响应中的 'code' (使用 HTTP 状态码)
            unified_code = response.status_code

            # 确定统一响应中的 'message'
            unified_message = "操作成功"  # 2xx 状态码的默认消息

            if 400 <= unified_code < 500:
                unified_message = "客户端请求错误"
                # 如果 original_data 是 FastAPI HTTPException 的 detail，尝试获取更具体的消息
                if isinstance(original_data, dict) and "detail" in original_data:
                    # 例如，如果 original_data 是 {"detail": "某个错误"}，则使用 "某个错误"
                    if isinstance(original_data["detail"], str):
                        unified_message = original_data["detail"]
                    # 例如，如果 original_data 是 {"detail": {"msg": "某个错误"}}
                    elif (
                        isinstance(original_data["detail"], dict)
                        and "msg" in original_data["detail"]
                        and isinstance(original_data["detail"]["msg"], str)
                    ):
                        unified_message = original_data["detail"]["msg"]
                    # 注意：这里我们决定将原始的错误负载（即使包含 "detail"）完整地放入 "data" 字段。
                    # 如果你希望 "data" 字段在有 "detail" 时为 null 或其他内容，可以在这里调整。

            elif 500 <= unified_code < 600:
                unified_message = "服务器内部错误"
                if isinstance(original_data, dict) and "detail" in original_data:
                    if isinstance(original_data["detail"], str):
                        unified_message = original_data["detail"]
                    elif (
                        isinstance(original_data["detail"], dict)
                        and "msg" in original_data["detail"]
                        and isinstance(original_data["detail"]["msg"], str)
                    ):
                        unified_message = original_data["detail"]["msg"]

            # 构建新的统一 JSON 内容
            unified_content = {
                "code": unified_code,
                "message": unified_message,
                "data": original_data,  # 如果原始响应体为空或格式错误，这里会是 None
            }

            # 使用统一的内容创建一个新的 JSONResponse
            # 保留原始的状态码和头部信息 (JSONResponse 会自动管理 Content-Type)
            new_response_headers = dict(response.headers)  # 创建头部信息的可变副本
            new_response = JSONResponse(
                content=unified_content,
                status_code=response.status_code,  # 保持原始状态码
                headers=new_response_headers,
            )
            return new_response

        # 如果响应类型不是 application/json，则按原样返回原始响应
        return response
