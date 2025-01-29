import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)
      
def get_users():
    users = load_json("users.json")
    return {"users": users}

def get_products():
    products = load_json("products.json")
    return {"products": products}