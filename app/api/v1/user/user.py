from fastapi import APIRouter
from app.api import login, register

router = APIRouter()

router.include_router(login.router, prefix="/user")
router.include_router(register.router, prefix="/user")
