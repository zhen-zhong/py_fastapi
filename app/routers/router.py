from fastapi import APIRouter
from app.api.v1.user.login import router as login_router
from app.api.v1.user.register import router as register_router

router = APIRouter()

router.include_router(login_router, prefix="/user")
router.include_router(register_router, prefix="/user")
