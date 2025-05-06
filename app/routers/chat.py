# routers/chat.py

from fastapi import APIRouter
from app.services.deepseek_service import get_deepseek_response
from app.models.request_models import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    接收聊天请求，调用 DeepSeek API 获取回复，并返回给客户端。
    """
    # 构建消息列表
    messages = [
        {"role": "system", "content": request.system_prompt},
        {"role": "user", "content": request.user_input},
    ]
    # 调用 DeepSeek API 获取回复
    reply = get_deepseek_response(messages)
    return ChatResponse(reply=reply)
