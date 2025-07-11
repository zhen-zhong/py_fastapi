from datetime import datetime, timedelta, timezone
from typing import Any, Union

from jose import jwt, JWTError
from passlib.context import CryptContext

# 警告: 实际项目中，这些值应该从 core/config.py 读取，config.py 再从 .env 文件读取
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_DAYS = 7     # 7 days
ALGORITHM = "HS256"
# 使用 openssl rand -hex 32 生成一个安全的密钥
JWT_SECRET_KEY = "your-super-secret-key"
JWT_REFRESH_SECRET_KEY = "your-super-secret-refresh-key"

# 密码哈希上下文
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + timedelta(days=expires_delta)
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None