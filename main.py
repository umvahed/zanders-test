from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import router

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the API routes
app.include_router(router)
