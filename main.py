from fastapi import FastAPI
from api import api

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
  
@app.get("/users")
def read_users():
    return api.get_users()

@app.get("/products")
def read_products():
    return api.get_products()