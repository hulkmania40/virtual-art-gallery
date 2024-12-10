from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = "mongodb+srv://admin:SVCSsvcs%402017@virtual-art-gallery.ttpyt.mongodb.net/"  # Use your connection string here
DB_NAME = "virtual_art_gallery"

# Create a MongoDB client
mongo_client = MongoClient(MONGO_URI)[DB_NAME]

