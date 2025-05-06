# main.py

from fastapi import FastAPI
from app.routers import chat

app = FastAPI()

# 包含聊天路由
app.include_router(chat.router)
