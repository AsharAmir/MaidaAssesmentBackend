from fastapi import HTTPException, status, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .database import tokens_collection
import secrets

security = HTTPBearer()


# Get the current token
async def get_current_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    token = credentials.credentials
    if not token:
        raise HTTPException(status_code=401, detail="Invalid auth header")
    doc = await tokens_collection.find_one({"token": token})
    if not doc:
        raise HTTPException(status_code=401, detail="Invalid token")
    return doc


# Get the current admin token
async def get_current_admin_token(token=Depends(get_current_token)):
    if not token.get("isAdmin"):
        raise HTTPException(status_code=403, detail="Admin only")
    return token


# Create a token string
def create_token_string():
    return secrets.token_urlsafe(32)
