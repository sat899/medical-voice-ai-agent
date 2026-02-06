from src.schemas.tts import (
    TTSClarificationRequest,
    TTSClarificationResponse,
    ClarificationQuestion,
)


async def generate_clarification_questions(
    payload: TTSClarificationRequest,
) -> TTSClarificationResponse:
    """
    Placeholder clarification logic.

    In the real implementation this would:
    - inspect the consultation text
    - propose structured questions grouped by category
    - optionally integrate with a TTS engine to generate audio
    """
    base_questions = [
        ClarificationQuestion(
            id="diagnosis-1",
            text="What is your working diagnosis?",
            category="diagnosis",
        ),
        ClarificationQuestion(
            id="safety-1",
            text="Are there any red flags or secondary symptoms you are concerned about?",
            category="safety-netting",
        ),
    ]

    return TTSClarificationResponse(questions=base_questions)

