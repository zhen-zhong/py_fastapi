# app/api/login.py
from fastapi import APIRouter
from app.schemas.user import UserLogin

router = APIRouter()


@router.post("/login")
def login(user: UserLogin):
    # 模拟登录逻辑
    if user.username == "admin" and user.password == "password":
        return {"message": "Login successful!"}
    return {"message": "Invalid credentials!"}
