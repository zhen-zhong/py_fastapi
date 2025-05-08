# main.py

from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.v1 import user

load_dotenv()
app = FastAPI()

# 包含用户相关的路由
app.include_router(user.router, prefix="/api/v1/user")


@app.get("/test")
def read_root():
    return {"message": "test"}
