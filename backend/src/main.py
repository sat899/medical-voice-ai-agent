from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Medical Voice AI Agent",
        version="0.1.0",
        description="Voice AI agent backend – LiveKit token endpoint and health check.",
    )

    # Allow Dawn UI served from localhost:3000 (and local file access) to call API
    origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost",
        "http://127.0.0.1",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
