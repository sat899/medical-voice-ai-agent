from src.schemas.agent import AgentOrchestratorRequest, AgentOrchestratorResponse
from src.schemas.actions import AgenticActionsRequest
from src.schemas.tts import TTSClarificationRequest
from src.services import stt as stt_service
from src.services import tts as tts_service
from src.services import actions as actions_service


async def run_orchestration(
    payload: AgentOrchestratorRequest,
) -> AgentOrchestratorResponse:
    """
    High-level orchestration function.

    This keeps the control flow separate from FastAPI endpoints so that
    people can iterate on orchestration logic in isolation.
    """
    result = AgentOrchestratorResponse()

    # NOTE: In a real implementation we would pass audio references here.
    # For now we operate on text only when provided.

    if payload.run_stt and payload.consultation_text:
        # Placeholder: pretend STT already ran and just wrap the text.
        # The real path would use an uploaded audio file.
        result.stt = await stt_service.transcribe_audio(
            audio=None,  # type: ignore[arg-type]
            metadata=None,
        )

    if payload.run_clarifications and payload.consultation_text:
        clar_req = TTSClarificationRequest(
            consultation_text=payload.consultation_text,
        )
        result.clarifications = await tts_service.generate_clarification_questions(
            clar_req
        )

    if payload.run_actions and payload.consultation_text:
        actions_req = AgenticActionsRequest(
            consultation_text=payload.consultation_text,
            structured_notes=result.stt.structured_notes if result.stt else None,
            consultant_answers=None,
        )
        result.actions = await actions_service.plan_agentic_actions(actions_req)

    return result

