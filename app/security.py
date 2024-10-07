from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .models import User
from .database import get_db

# A very simple authentication function
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username, User.hashed_password == password).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return user
