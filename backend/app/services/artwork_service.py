from app.db import mongo_client
from app.models import Artwork
from fastapi import HTTPException
from bson.objectid import ObjectId

ARTWORK_COLLECTION = "artworks"  # MongoDB collection name for artworks


def get_artworks(skip: int = 0, limit: int = 10):
    """
    Get a list of artworks with pagination.
    """
    artworks = mongo_client[ARTWORK_COLLECTION].find().skip(skip).limit(limit)
    return list(artworks)  # Convert cursor to list


def get_artwork_by_id(artwork_id: str):
    """
    Get a single artwork by its ID.
    """
    if not ObjectId.is_valid(artwork_id):
        raise HTTPException(status_code=400, detail="Invalid artwork ID format")

    artwork = mongo_client[ARTWORK_COLLECTION].find_one({"_id": ObjectId(artwork_id)})
    if not artwork:
        raise HTTPException(status_code=404, detail="Artwork not found")

    return artwork


def add_artwork(artwork: Artwork):
    """
    Add a new artwork to the collection.
    """
    artwork_dict = artwork.dict(exclude_unset=True)  # Convert Pydantic model to dict, excluding defaults
    result = mongo_client[ARTWORK_COLLECTION].insert_one(artwork_dict)

    # Return the newly added artwork with its ID
    artwork_dict["_id"] = result.inserted_id
    return artwork_dict


def update_artwork(artwork_id: str, artwork: Artwork):
    """
    Update an existing artwork in the collection.
    """
    if not ObjectId.is_valid(artwork_id):
        raise HTTPException(status_code=400, detail="Invalid artwork ID format")

    updated_artwork = artwork.dict(exclude_unset=True)
    result = mongo_client[ARTWORK_COLLECTION].update_one(
        {"_id": ObjectId(artwork_id)},
        {"$set": updated_artwork},
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Artwork not found")

    return {"message": "Artwork updated successfully"}


def delete_artwork(artwork_id: str):
    """
    Delete an artwork by its ID.
    """
    if not ObjectId.is_valid(artwork_id):
        raise HTTPException(status_code=400, detail="Invalid artwork ID format")

    result = mongo_client[ARTWORK_COLLECTION].delete_one({"_id": ObjectId(artwork_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Artwork not found")

    return {"message": "Artwork deleted successfully"}
