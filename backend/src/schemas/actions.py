from typing import List, Optional

from pydantic import BaseModel


class AgenticActionsRequest(BaseModel):
    consultation_text: str
    structured_notes: Optional[str] = None
    consultant_answers: Optional[dict] = None


class PlannedAction(BaseModel):
    type: str  # e.g. "order_test", "draft_letter", "schedule_appointment"
    description: str
    payload: dict  # free-form details; should be further structured later


class AgenticActionsResponse(BaseModel):
    actions: List[PlannedAction]

