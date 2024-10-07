from pydantic import BaseModel
from datetime import datetime

class UserLogin(BaseModel):
    username: str
    password: str

class MessageCreate(BaseModel):
    content: str

class MessageResponse(BaseModel):
    username: str
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True
