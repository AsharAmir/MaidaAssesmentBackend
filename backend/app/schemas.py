from pydantic import BaseModel


class TokenCreateRequest(BaseModel):
    """
    Schema for the request to create a token
    """

    isAdmin: bool = False


class TokenResponse(BaseModel):
    """
    Schema for the response to create a token
    """

    token: str
    isAdmin: bool


class ModerateResponse(BaseModel):
    """
    Schema for the response to moderate a text
    """

    categories: dict
    confidence: dict
