from fastapi import APIRouter, UploadFile, File

from src.schemas.stt import STTRequestMetadata, STTResponse
from src.services.stt import transcribe_audio

router = APIRouter()


@router.post("/transcribe", response_model=STTResponse)
async def transcribe(
    audio: UploadFile = File(...),
    metadata: STTRequestMetadata | None = None,
) -> STTResponse:
    """
    STT endpoint: given an audio file (e.g. recorded consultation),
    return a raw transcription and a structured note draft.
    """
    # NOTE: metadata can carry language, patient id, consultant id, etc.
    result = await transcribe_audio(audio=audio, metadata=metadata)
    return result

