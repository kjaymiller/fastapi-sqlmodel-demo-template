import os
from typing import Sequence
from .models import Item
from sqlmodel import Session, create_engine, SQLModel, select
from sqlalchemy.engine import Engine

engine = create_engine(os.getenv("DB_URI", "sqlite:///database.db"))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def create_item(*, item: Item, session) -> Item:
    session.add(item)
    session.commit()
    return item

def get_item(*, item_id: int, session) -> Item | None:
    item = session.get(Item, item_id)
    return item

def all_items(session) -> Sequence[Item]:
    query = select(Item)
    items = session.exec(query).all()
    return items

def update_item(*, item_id: int, item: Item, session) -> Item:
    item = session.get(Item, item_id)
    item.name = item.name
    item.quantity = item.quantity
    session.add(item)
    session.commit()
    return item

def delete_item(item_id: int, session) -> Item:
    item = session.get(Item, item_id)
    session.delete(item)
    session.commit()
    return item

def get_items_by(item_filters: dict, session) -> list[Item]:
    item = session.exec(Item).filter_by(**item_filters)
    return item

def query_items(query: str, session) -> list[Item]:
    items = session.exec(Item).where(query)
    return items