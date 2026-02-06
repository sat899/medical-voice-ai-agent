from fastapi import APIRouter

from src.schemas.tts import TTSClarificationRequest, TTSClarificationResponse
from src.services.tts import generate_clarification_questions

router = APIRouter()


@router.post("/clarifications", response_model=TTSClarificationResponse)
async def clarifications(
    payload: TTSClarificationRequest,
) -> TTSClarificationResponse:
    """
    Given consultation notes / transcript and context about the case,
    propose structured clarification questions for the consultant.
    """
    return await generate_clarification_questions(payload)

