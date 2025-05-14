from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers.router import router as main_router
from app.utils.response_middleware import UnifiedJsonResponseMiddleware
from app.utils.add_headers_middleware import AddResponseHeadersMiddleware

load_dotenv()

app = FastAPI()
app.add_middleware(AddResponseHeadersMiddleware)
app.add_middleware(UnifiedJsonResponseMiddleware)

app.include_router(main_router, prefix="/api/v1")

@app.get("/test")
def read_root():
    return {"message": "Hello, world"}
