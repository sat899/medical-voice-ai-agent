"""
API Routes: Consultation Agent
Endpoints for driving the consultation workflow with Claude LLM
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.services.claude_consultation import process_consultation

router = APIRouter()


class ConsultationStartRequest(BaseModel):
    """Request to start consultation analysis"""
    bypass_next_steps_prompt: bool = False


class ConsultationStartResponse(BaseModel):
    """Response with transcription and next steps prompt"""
    transcription: str
    next_steps_prompt: str


class DraftLetterRequest(BaseModel):
    """Request to draft the consultation letter"""
    doctor_next_steps: str
    patient_name: str = "Patient"
    consultant_name: str = "Dr. [Name]"


class DraftLetterResponse(BaseModel):
    """Response with drafted letter"""
    letter: str


@router.post("/consultation/start", response_model=ConsultationStartResponse)
async def start_consultation(request: ConsultationStartRequest):
    """
    Start the consultation workflow:
    - Read the transcription
    - Generate a prompt asking doctor about next steps
    """
    try:
        result = process_consultation()
        return ConsultationStartResponse(
            transcription=result["transcription"],
            next_steps_prompt=result["next_steps_prompt"]
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing consultation: {str(e)}")


@router.post("/consultation/draft-letter", response_model=DraftLetterResponse)
async def draft_letter(request: DraftLetterRequest):
    """
    Draft the consultation letter based on doctor's next steps
    """
    try:
        result = process_consultation(doctor_response=request.doctor_next_steps)
        if not result["letter"]:
            # Draft the letter if not already done
            from src.services.claude_consultation import draft_letter as draft_letter_fn
            from src.services.claude_consultation import read_transcription as read_trans
            transcription = read_trans()
            letter = draft_letter_fn(
                transcription, 
                request.doctor_next_steps,
                request.patient_name,
                request.consultant_name
            )
            return DraftLetterResponse(letter=letter)
        return DraftLetterResponse(letter=result["letter"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error drafting letter: {str(e)}")
