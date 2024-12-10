from fastapi import APIRouter, HTTPException
from app.services.artwork_service import (
    get_artworks,
    get_artwork_by_id,
    add_artwork,
    update_artwork,
    delete_artwork
)
from app.models import Artwork

router = APIRouter()

@router.get("/artworks")
async def list_artworks(skip: int = 0, limit: int = 10):
    return get_artworks(skip, limit)

@router.get("/artworks/{artwork_id}")
async def read_artwork(artwork_id: str):
    return get_artwork_by_id(artwork_id)

@router.post("/artworks")
async def create_artwork(artwork: Artwork):
    return add_artwork(artwork)

@router.put("/artworks/{artwork_id}")
async def update_art(artwork_id: str, artwork: Artwork):
    return update_artwork(artwork_id, artwork)

@router.delete("/artworks/{artwork_id}")
async def delete_art(artwork_id: str):
    return delete_artwork(artwork_id)
