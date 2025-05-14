from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class AddResponseHeadersMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # 1. 调用请求处理链中的下一个环节，获取原始的响应对象
        response = await call_next(request)

        # 2. 在获取到的响应对象上添加自定义的响应标头
        # 这些标头将包含在从服务器发送到客户端的 HTTP 响应中
        response.headers["X-App-Version"] = "1.2.3"
        response.headers["X-Powered-By"] = "MyAwesomeFramework"
        response.headers["Cache-Control"] = (
            "no-cache, no-store, must-revalidate"  # 示例：控制缓存
        )
        response.headers["Pragma"] = "no-cache"  # 兼容旧版 HTTP/1.0 缓存
        response.headers["Expires"] = "0"  # 确保不被缓存

        # 3. 返回修改了标头的响应对象
        return response
