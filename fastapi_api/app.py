from sqlmodel import Session
from . import db

from fastapi import Depends, FastAPI
from .models import Item

app = FastAPI()

@app.get("/")
def root():
    """Returns a welcome message to the API."""
    return {"message": "Welcome to the API"}

@app.get("/items")
def all_items(*, session: Session = Depends(db.get_session)):
    """Returns all items currently in the database"""
    items = db.all_items(session=session)
    return {
        "message": "Items retrieved successfully",
        "data": items
        }

@app.post("/item")
def create_item(*,
    item: Item,
    session: Session = Depends(db.get_session),
):
    """Creates a new item in the database."""

    new_item = db.create_item(session=session, item=item)
    return {
        "message": "Item created successfully",
        "data": new_item
        }

@app.get("/item/{item_id}")
def get_item(*,
    session: Session = Depends(db.get_session),
    item_id: str,
):
    """Returns a single item from the database based on the `id`."""
    item = db.get_item(session=session, item_id=item_id)
    return {
        "message": "Item retrieved successfully",
        "data": item
    }

@app.put("/item/{item_id}")
def update_item(
    *, 
    session: Session = Depends(db.get_session),
    item_id: str, item: Item,
    ):
    """Updates a single item from the database based on the `id`."""
    item = db.update_item(
        session=session,
        item_id=item_id,
        item=item,
        )
    return {
        "message": "Item updated successfully",
        "data": item
    }

@app.delete("/items/{item_id}")
def delete_item(
    *,
    session: Session = Depends(db.get_session),
    item_id: str):
    Item.objects(session=session, id=item_id).delete()
    return {"message": "Item deleted successfully"}