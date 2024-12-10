# app/routes/users.py
from fastapi import APIRouter, HTTPException
from app.db import mongo_client
from app.models import User  # MongoDB client

router = APIRouter()

# POST route for user registration
@router.post("/users/")
async def create_user(user: User):
    # Check if the user already exists
    existing_user = mongo_client["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Insert new user into the database
    mongo_client["users"].insert_one(user.dict())  # Convert Pydantic model to dict
    return {"message": "User created successfully", "user": user}
