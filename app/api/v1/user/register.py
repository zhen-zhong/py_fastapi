from fastapi import APIRouter
from app.schemas.user import UserRegister

router = APIRouter()


@router.post("/register")
def register(user: UserRegister):
    # 模拟注册逻辑
    return {"message": f"User {user.username} registered successfully!"}
