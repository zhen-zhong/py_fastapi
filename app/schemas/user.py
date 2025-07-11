# app/schemas/user.py

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    id: int

    class Config:
        from_attributes = True # Pydantic v2, or orm_mode = True for v1