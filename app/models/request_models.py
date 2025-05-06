# models/request_models.py

from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_input: str
    system_prompt: str = "你好！"


class ChatResponse(BaseModel):
    reply: str
