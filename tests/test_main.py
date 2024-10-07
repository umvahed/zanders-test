import pytest
from fastapi.testclient import TestClient
from .main import app
from .database import Base, engine, SessionLocal
from .models import User

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Create a test user
    test_user = User(username="testuser", hashed_password="testpassword")
    db.add(test_user)
    db.commit()
    db.close()

    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_login_success(client, test_db):
    response = client.post("/login", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert response.cookies.get("session") == "testuser"

def test_login_invalid_credentials(client, test_db):
    response = client.post("/login", json={"username": "testuser", "password": "wrongpassword"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid username or password"}

def test_post_message_without_login(client, test_db):
    response = client.post("/message", json={"content": "Hello, world!"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

# def test_post_empty_message(client, test_db):
    # First, login
    # assert response.status_code == 400
    # assert response.json() == {"detail": "Message content cannot be empty"}

# def test_get_messages_success(client, test_db):
    # Login and post a message
    # Retrieve messages
    # assert response.status_code == 200
    # assert response.json()[0]["content"] == "Test message"

# def test_get_messages_no_content(client, test_db):
    # Login as a different user with no messages
    # assert response.status_code == 404
    # assert response.json() == {"detail": "No messages found"}
