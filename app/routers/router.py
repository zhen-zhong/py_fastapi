from fastapi import APIRouter
from app.api.v1.user.login import router as login_router
from app.api.v1.user.register import router as register_router
from app.api.v1.user.downLoadMP4 import router as get_video_src_router
router = APIRouter()

router.include_router(login_router, prefix="/user")
router.include_router(register_router, prefix="/user")
router.include_router(get_video_src_router, prefix="/user")
