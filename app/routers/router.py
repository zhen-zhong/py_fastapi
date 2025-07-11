# app/api/router.py

from fastapi import APIRouter
from app.api.v1.endpoints import login, users

# 创建一个总的 API 路由器，通常我们会给它一个更明确的名字
api_router = APIRouter()

# 修正：使用 'login.router' 而不是 'login_router'
# 同时，我们将 login 路由挂载到更合理的前缀 '/login' 下
api_router.include_router(login.router, prefix="/login", tags=["Authentication"])

# 补充：将 users 路由也包含进来
api_router.include_router(users.router, prefix="/users", tags=["Users"])

# 注意：原来的 'router' 变量名已改为 'api_router'，以避免与导入的模块中的 'router' 混淆。