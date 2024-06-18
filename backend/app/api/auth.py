from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(user: User):
    # Add your authentication logic here
    return {"message": "Login successful"}
