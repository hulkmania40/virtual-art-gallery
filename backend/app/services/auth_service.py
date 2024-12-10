import hashlib
import hmac
from fastapi import HTTPException

SECRET_KEY = b'supersecretkey'  # Replace with your secret key
HASH_ALGORITHM = "sha256"  # You can also use "sha512"


def hash_password(password: str) -> str:
    """
    Hash the password using hashlib.
    """
    hashed = hashlib.new(HASH_ALGORITHM)
    hashed.update(password.encode('utf-8'))
    return hashed.hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify the password by comparing its hash with the stored hash.
    """
    return hash_password(password) == hashed_password


def create_access_token(data: dict) -> str:
    """
    Generate an HMAC token using the secret key.
    """
    message = str(data).encode("utf-8")
    token = hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()
    return token
