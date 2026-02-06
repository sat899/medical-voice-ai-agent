from datetime import datetime

from fastapi import UploadFile

from src.schemas.stt import STTRequestMetadata, STTResponse


async def transcribe_audio(
    audio: UploadFile,
    metadata: STTRequestMetadata | None,
) -> STTResponse:
    """
    Placeholder STT implementation.

    In the real implementation this would:
    - stream audio chunks to an STT provider
    - optionally translate to target language
    - run note-generation over the transcript
    """
    fake_transcript = f"Transcribed text for file={audio.filename!r}"
    fake_notes = (
        "Patient attended consultation. This is a placeholder structured note "
        "generated from the transcript."
    )

    return STTResponse(
        raw_transcript=fake_transcript,
        structured_notes=fake_notes,
        created_at=datetime.utcnow(),
    )

