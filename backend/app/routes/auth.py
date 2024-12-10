from fastapi import APIRouter, HTTPException
from app.db import mongo_client  # Import mongo_client
from app.services.auth_service import hash_password, verify_password, create_access_token
from app.models import User

router = APIRouter()

@router.post("/register")
async def register(user: User):
    # Check if the user already exists
    existing_user = mongo_client["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password before storing
    user.password = hash_password(user.password)
    mongo_client["users"].insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: User):
    # Fetch the user from the database
    db_user = mongo_client["users"].find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Verify the password
    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Create an access token
    token = create_access_token({"email": user.email})
    return {"access_token": token, "token_type": "bearer"}