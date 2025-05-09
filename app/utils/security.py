import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 从 .env 文件中获取 SECRET_KEY、ALGORITHM 和 ACCESS_TOKEN_EXPIRE_DAYS
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_DAYS = int(os.getenv("ACCESS_TOKEN_EXPIRE_DAYS", 7))


def create_access_token(
    username: str,
    user_id: int,
    created_at: str,
    expires_delta: timedelta = timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS),
):
    # 将创建时间和过期时间转换为时间戳
    created_at_timestamp = int(
        datetime.now(timezone.utc).timestamp()
    )  # 当前时间的时间戳（UTC）
    expire_timestamp = int(
        (datetime.now(timezone.utc) + expires_delta).timestamp()
    )  # 过期时间的时间戳（UTC）

    to_encode = {
        "sub": username,
        "user_id": user_id,
        "created_at": created_at_timestamp,
        "exp": expire_timestamp,
    }

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def parse_jwt_token(token: str):
    try:
        # 解码 token 并验证
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        user_id = payload.get("user_id")
        created_at_timestamp = payload.get("created_at")
        expire_time_timestamp = payload.get("exp")

        # 检查是否提取到必要的字段
        if not all([username, user_id, created_at_timestamp, expire_time_timestamp]):
            raise HTTPException(status_code=401, detail="Invalid token")

        return {
            "username": username,
            "user_id": user_id,
            "created_at": created_at_timestamp,
            "expire_time": expire_time_timestamp,
        }

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
