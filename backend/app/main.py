from fastapi import FastAPI
from .auth import router as auth_router
from .moderation import router as moderation_router
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="Image Moderation API",
    swagger_ui_init_oauth={"usePkceWithAuthorizationCodeGrant": True},
    openapi_tags=[{"name": "auth"}, {"name": "moderation"}],
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url=None,
)

bearer_scheme = HTTPBearer()

# Add security scheme to OpenAPI
app.openapi_schema = None


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "HTTPBearer": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    for path in openapi_schema["paths"].values():
        for op in path.values():
            op["security"] = [{"HTTPBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore[assignment]

# Include the routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(moderation_router, tags=["moderation"])
