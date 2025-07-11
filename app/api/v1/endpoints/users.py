# app/api/v1/endpoints/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserPublic
from app.crud.user import create_user, get_user_by_username
from app.api.v1.deps import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register_new_user(user_in: UserCreate):
    user = get_user_by_username(username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    new_user = create_user(user_in=user_in)
    return new_user

@router.get("/me", response_model=UserPublic)
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Get current user.
    """
    return current_user