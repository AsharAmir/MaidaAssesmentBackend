from fastapi import APIRouter, File, UploadFile, Depends
from .database import usages_collection
from .utils import get_current_token
from .schemas import ModerateResponse
from datetime import datetime

router = APIRouter()


@router.post("/moderate", response_model=ModerateResponse)
async def moderate_image(
    file: UploadFile = File(...), token=Depends(get_current_token)
):
    # Dummy moderation logic
    categories = {"nudity": False, "violence": False, "hate": False}
    confidence = {"nudity": 0.01, "violence": 0.01, "hate": 0.01}
    await usages_collection.insert_one(
        {
            "token": token["token"],
            "endpoint": "/moderate",
            "timestamp": datetime.utcnow(),
        }
    )
    return ModerateResponse(categories=categories, confidence=confidence)
