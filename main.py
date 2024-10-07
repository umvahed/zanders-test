# main.py
from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the API routes
app.include_router(router)