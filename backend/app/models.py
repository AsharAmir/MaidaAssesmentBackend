from pydantic import BaseModel, Field
from datetime import datetime


class TokenModel(BaseModel):
    """
    Schema for the token model
    """

    token: str
    isAdmin: bool = False
    createdAt: datetime = Field(default_factory=datetime.utcnow)


class UsageModel(BaseModel):
    """
    Schema for the usage model
    """

    token: str
    endpoint: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
