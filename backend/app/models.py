from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class Artwork(BaseModel):
    title: str
    description: Optional[str]
    tags: List[str]
    image_url: str
    artist: str

class Comment(BaseModel):
    user_id: str
    artwork_id: str
    content: str
