from . import db

from fastapi import FastAPI
from .models import Item

app = FastAPI()

@app.get("/")
def root():
    """Returns a welcome message to the API."""
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
    """Creates a new item in the database."""
    new_item = db.create_item(item)
    return {
        "message": "Item created successfully",
        "data": new_item
        }

@app.get("/items/{item_id}")
def get_item(item_id: str):
    """Returns a single item from the database based on the `id`."""
    item = db.get_item(item_id)
    return {
        "message": "Item retrieved successfully",
        "data": item
    }

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    """Updates a single item from the database based on the `id`."""
    item = db.update_item(item_id, item)
    return {
        "message": "Item updated successfully",
        "data": item
    }

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    Item.objects(id=item_id).delete()
    return {"message": "Item deleted successfully"}