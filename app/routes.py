from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, security
from .database import get_db

router = APIRouter()

# Login endpoint that checks if credentials are correct (but does not set cookies)
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    authenticated_user = security.authenticate_user(db, user.username, user.password)
    return {"message": "Login successful", "username": authenticated_user.username}

# Post message (requires login credentials in the request body)
@router.post("/message", response_model=schemas.MessageResponse)
def create_message(
    message: schemas.MessageCreate,
    user: schemas.UserLogin,  # User sends credentials with each request
    db: Session = Depends(get_db)
):
    authenticated_user = security.authenticate_user(db, user.username, user.password)
    db_message = models.Message(content=message.content, user_id=authenticated_user.id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# Get all messages (requires login credentials in the request body)
@router.get("/message", response_model=list[schemas.MessageResponse])
def get_messages(user: schemas.UserLogin, db: Session = Depends(get_db)):
    authenticated_user = security.authenticate_user(db, user.username, user.password)
    messages = db.query
    return messages