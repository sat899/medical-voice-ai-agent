from fastapi import FastAPI

from src.api.routes import router as api_router
from src.core.config import settings


def create_app() -> FastAPI:
    """
    Application factory. Attach routers and shared dependencies here.
    """
    app = FastAPI(
        title="Medical Voice AI Agent",
        version="0.1.0",
        description="Post-consultation scribe, research, and action support API.",
    )

    # Mount versioned API router
    app.include_router(api_router, prefix="/api")

    return app


app = create_app()

