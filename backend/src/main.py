from fastapi import FastAPI

from src.api.routes import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Medical Voice AI Agent",
        version="0.1.0",
        description="Voice AI agent backend – LiveKit token endpoint and health check.",
    )
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
