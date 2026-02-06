from fastapi import APIRouter

from src.api.v1 import stt, tts, actions, health, agent

router = APIRouter()

router.include_router(health.router, prefix="/v1/health", tags=["health"])
router.include_router(stt.router, prefix="/v1/stt", tags=["stt"])
router.include_router(tts.router, prefix="/v1/tts", tags=["tts"])
router.include_router(actions.router, prefix="/v1/actions", tags=["actions"])
router.include_router(agent.router, prefix="/v1/agent", tags=["agent"])

