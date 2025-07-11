# app/crud/user.py

from typing import Optional
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_hashed_password

# --- 模拟数据库 ---
db_users = {}
next_user_id = 1
# ------------------

def get_user_by_username(username: str) -> Optional[User]:
    for user in db_users.values():
        if user.username == username:
            return user
    return None

def create_user(user_in: UserCreate) -> User:
    global next_user_id
    hashed_password = get_hashed_password(user_in.password)
    new_user = User(
        id=next_user_id,
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password,
    )
    db_users[next_user_id] = new_user
    next_user_id += 1
    return new_user