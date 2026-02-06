from typing import List, Optional

from pydantic import BaseModel


class TTSClarificationRequest(BaseModel):
    consultation_text: str
    provisional_diagnosis: Optional[str] = None
    secondary_symptoms: Optional[List[str]] = None


class ClarificationQuestion(BaseModel):
    id: str
    text: str
    category: str  # e.g. "diagnosis", "safety-netting", "follow-up"


class TTSClarificationResponse(BaseModel):
    questions: List[ClarificationQuestion]

