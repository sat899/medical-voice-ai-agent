from fastapi import APIRouter

from src.schemas.actions import (
    AgenticActionsRequest,
    AgenticActionsResponse,
)
from src.services.actions import plan_agentic_actions

router = APIRouter()


@router.post("/", response_model=AgenticActionsResponse)
async def plan_actions(
    payload: AgenticActionsRequest,
) -> AgenticActionsResponse:
    """
    Given consultation data + clarifications, decide next steps:
    - draft letters
    - order tests
    - schedule follow-ups / waiting list decisions
    """
    return await plan_agentic_actions(payload)

