from fastapi import FastAPI

app = FastAPI()

# 创建一个根路由
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# 创建一个带路径参数的路由
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
