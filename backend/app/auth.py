from fastapi import APIRouter, HTTPException, Depends
from .database import tokens_collection
from .schemas import TokenCreateRequest, TokenResponse
from .utils import get_current_admin_token, create_token_string
from datetime import datetime

router = APIRouter()


@router.post("/tokens", response_model=TokenResponse)
async def create_token(
    data: TokenCreateRequest,
    admin=Depends(get_current_admin_token),
):
    """
    Create a token, only admin can create a token
    """
    token = create_token_string()
    doc = {
        "token": token,
        "isAdmin": data.isAdmin,
        "createdAt": datetime.utcnow(),
    }
    await tokens_collection.insert_one(doc)
    return TokenResponse(token=token, isAdmin=data.isAdmin)


@router.get("/tokens", response_model=list[TokenResponse])
async def list_tokens(admin=Depends(get_current_admin_token)):
    """
    List all tokens, only admin can list tokens
    """
    tokens = await tokens_collection.find().to_list(100)
    # RBAC
    return [TokenResponse(token=t["token"], isAdmin=t["isAdmin"]) for t in tokens]


@router.delete("/tokens/{token}")
async def delete_token(token: str, admin=Depends(get_current_admin_token)):
    """
    Delete a token, only admin can delete a token
    """
    result = await tokens_collection.delete_one({"token": token})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Token not found")
    return {"detail": "Token deleted"}
