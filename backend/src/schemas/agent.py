from typing import Optional

from pydantic import BaseModel

from src.schemas.actions import AgenticActionsResponse
from src.schemas.stt import STTResponse
from src.schemas.tts import TTSClarificationResponse


class AgentOrchestratorRequest(BaseModel):
    """
    High-level request where frontend can send:
    - reference to an uploaded audio file (or text)
    - flags for which capabilities to run
    """

    consultation_text: Optional[str] = None
    run_stt: bool = True
    run_clarifications: bool = True
    run_actions: bool = True


class AgentOrchestratorResponse(BaseModel):
    stt: Optional[STTResponse] = None
    clarifications: Optional[TTSClarificationResponse] = None
    actions: Optional[AgenticActionsResponse] = None

