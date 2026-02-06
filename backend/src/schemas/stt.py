from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class STTRequestMetadata(BaseModel):
    language: str = "en"
    patient_id: Optional[str] = None
    consultant_id: Optional[str] = None
    appointment_id: Optional[str] = None


class STTResponse(BaseModel):
    raw_transcript: str
    structured_notes: str
    created_at: datetime

