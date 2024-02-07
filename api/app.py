from . import db

from fastapi import FastAPI
from .models import Item

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/items")
def all_items():
    """Returns all items currently in the database"""
    items = db.all_items()
    return {
        "message": "Items retrieved successfully",
        "data": items
        }

@app.post("/items")
def create_item(item: Item):
    new_item = db.create_item(item)
    return {
        "message": "Item created successfully",
        "data": new_item
        }

@app.get("/items/{item_id}")
def get_item(item_id: str):
    return Item.objects(id=item_id).to_json()

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    Item.objects(id=item_id).update(**item.dict())
    return Item.objects(id=item_id).to_json()

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    Item.objects(id=item_id).delete()
    return {"message": "Item deleted successfully"}