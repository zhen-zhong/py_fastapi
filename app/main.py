from fastapi import FastAPI

# 导入 FastAPI 和数据库连接函数
from app.db.init_db import get_db_connection

app = FastAPI()

# 创建一个根路由
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/test")
async def read_root():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM detail_info LIMIT 1")
            result = cursor.fetchone()
            return {"data": result}
    finally:
        
        connection.close()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 创建一个 POST 请求路由
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price, "tax": item.tax}
