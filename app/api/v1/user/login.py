from fastapi import APIRouter, HTTPException
from app.utils.security import create_access_token
from datetime import datetime, timezone

router = APIRouter()


@router.post("/login")
def login():
    # 使用字典定义用户信息
    user = {"username": "admin", "password": "password"}
    print("用户信息:", user)

    # 使用字典的键来访问数据
    if user["username"] == "admin" and user["password"] == "password":
        # 假设用户 ID 和创建时间（你可以从数据库获取真实数据）
        user_id = 1  # 这里假设用户 ID 是 1
        created_at = datetime.now(timezone.utc)  # 使用当前时间作为创建时间

        # 生成 token
        access_token = create_access_token(
            username=user["username"], user_id=user_id, created_at=created_at
        )

        return {"access_token": access_token, "token_type": "bearer"}

    # 如果用户名或密码错误，返回 401 错误
    raise HTTPException(status_code=401, detail="Invalid credentials")
