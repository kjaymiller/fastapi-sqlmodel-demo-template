import os
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool

from fastapi_api.models import Item
from fastapi_api import db
from fastapi_api.app import app

client = TestClient(app)

@pytest.fixture(scope="session")
def config_db():
    """Load test data into the database."""
    engine = create_engine(
        "sqlite://",  
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture(scope="session", autouse=True)
def test_client(config_db):
    def get_session_override():
        return session

    app.dependency_overrides[db.get_session] = get_session_override
    client = TestClient    
    session = Session(config_db)
    db.create_item(session=session, item=Item(name="Jay", quantity=42))
    db.create_item(session=session, item=Item(name="Jason", quantity=42))
    yield client
    app.dependency_overrides.clear()
        
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the API"

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Items retrieved successfully",
        "data": [
            {"id": 1, "name": "Jay", "quantity": 42},
            {"id": 2, "name": "Jason", "quantity": 42},
        ],
    }

def test_read_item():
    response = client.get("/item/1")
    assert response.status_code == 200