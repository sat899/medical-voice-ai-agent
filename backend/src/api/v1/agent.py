from fastapi import APIRouter

from src.schemas.agent import AgentOrchestratorRequest, AgentOrchestratorResponse
from src.agents.orchestrator import run_orchestration

router = APIRouter()


@router.post("/run", response_model=AgentOrchestratorResponse)
async def run_agent(
    payload: AgentOrchestratorRequest,
) -> AgentOrchestratorResponse:
    """
    High-level orchestration endpoint.
    Orchestrates:
    - STT (scribing)
    - clarification questions (TTS)
    - agentic actions (letters, tests, appointments)
    """
    return await run_orchestration(payload)

