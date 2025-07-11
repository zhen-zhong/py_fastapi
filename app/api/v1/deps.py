# app/api/v1/deps.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.core.security import ALGORITHM, JWT_SECRET_KEY
from app.schemas.token import TokenPayload
from app.crud.user import get_user_by_username
from app.models.user import User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/api/v1/login"  # 指向登录接口
)

def get_current_user(token: str = Depends(reusable_oauth2)) -> User:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (JWTError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = get_user_by_username(username=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user