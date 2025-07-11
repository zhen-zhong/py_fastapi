# app/api/v1/endpoints/login.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import create_access_token, create_refresh_token, verify_password
from app.crud.user import get_user_by_username
from app.schemas.token import Token

router = APIRouter()

@router.post("", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(username=form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    return {
        "access_token": create_access_token(user.username),
        "refresh_token": create_refresh_token(user.username),
    }