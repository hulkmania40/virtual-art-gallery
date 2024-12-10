from fastapi import FastAPI
from app.routes import auth, artworks, users

app = FastAPI()

# Include API routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(artworks.router, prefix="/api/artworks", tags=["Artworks"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Virtual Art Gallery API"}
