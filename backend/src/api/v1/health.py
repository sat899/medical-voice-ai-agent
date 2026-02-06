from fastapi import APIRouter

from src.schemas.health import HealthResponse

router = APIRouter()


@router.get("/", response_model=HealthResponse)
async def read_health() -> HealthResponse:
    """
    Simple healthcheck. Useful for infra / monitoring and quick sanity checks.
    """
    return HealthResponse(status="ok")

