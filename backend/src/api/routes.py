from fastapi import APIRouter

from src.api.v1 import health, livekit

router = APIRouter()

router.include_router(health.router, prefix="/v1/health", tags=["health"])
router.include_router(livekit.router, prefix="/v1/livekit", tags=["livekit"])
