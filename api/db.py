from .models import Item
from sqlmodel import Session, create_engine, SQLModel, select

db = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(db)


def create_item(item: Item):
    with Session(db) as session:
        session.add(item)
        session.commit()
    return item

def get_item(item_id: int):
    with Session(db) as session:
        item = session.get(Item, item_id)
    return item

def all_items():
    with Session(db) as session:
        query = select(Item)
        items = session.exec(query).all()
    return items

def update_item(item_id: int, item: Item):
    with Session(db) as session:
        item = session.get(Item, item_id)
        item.name = item.name
        item.quantity = item.quantity
        session.add(item)
        session.commit()
    return item

def delete_item(item_id: int):
    with Session(db) as session:
        item = session.get(Item, item_id)
        session.delete(item)
        session.commit()
    return item

def get_items_by(item_filters: dict):
    with Session(db) as session:
        item = session.exec(Item).filter_by(**item_filters)
    return item

def query_items(query: str):
    with Session(db) as session:
        items = session.exec(Item).where(query)
    return items