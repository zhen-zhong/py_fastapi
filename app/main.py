from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers.router import router as main_router
load_dotenv()
app = FastAPI()

# 包含用户相关的路由
app.include_router(main_router, prefix="/api/v1")


@app.get("/test")
def read_root():
    return {"message": "test"}
