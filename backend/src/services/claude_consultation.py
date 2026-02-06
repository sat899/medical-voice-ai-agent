"""
Service: Claude Consultation Assistant
Integrates Claude LLM for:
- Analyzing consultation transcripts
- Generating prompts for clinician about next steps
- Drafting consultation letters with template
"""

import os
from pathlib import Path
from datetime import datetime
import anthropic


def _get_client() -> anthropic.Anthropic:
    """Lazy-initialise the Anthropic client (avoids import-time crashes)."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")
    return anthropic.Anthropic(api_key=api_key)

TRANSCRIPTION_PATH = Path(__file__).parent / "outputs" / "transcription.txt"
TEMPLATE_PATH = Path(__file__).parent / "templates" / "consultation_letter.md"


def read_transcription(filepath: Path = TRANSCRIPTION_PATH) -> str:
    """Read the consultation transcription from file."""
    if not filepath.exists():
        raise FileNotFoundError(f"Transcription file not found: {filepath}")
    return filepath.read_text(encoding="utf-8")


def generate_next_steps_prompt(transcription: str) -> str:
    """
    Use Claude to analyze the transcription and generate a prompt 
    asking the doctor about recommended next steps.
    """
    message = _get_client().messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a clinical assistant helping a doctor document consultation notes.

Here is a transcription of the consultation:

<transcription>
{transcription}
</transcription>

Based on this consultation, generate a friendly but professional prompt asking the doctor 
what clinical next steps they would like to plan (e.g., blood tests, imaging, referrals, 
follow-up appointment, lifestyle advice, medications).

The prompt should be conversational and suitable for voice-based interaction.
Keep it to 2-3 sentences maximum."""
            }
        ]
    )
    return message.content[0].text


def draft_letter(transcription: str, doctor_next_steps: str, patient_name: str = "Patient", consultant_name: str = "Dr. [Name]") -> str:
    """
    Use Claude to draft a consultation letter based on the transcription 
    and the doctor's confirmed next steps.
    """
    template = TEMPLATE_PATH.read_text(encoding="utf-8") if TEMPLATE_PATH.exists() else None
    template_section = f"Template Format:\n{template}" if template else ""

    message = _get_client().messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"""You are a medical letter writing assistant. Draft a professional consultation summary letter.

Consultation Transcription:
<transcription>
{transcription}
</transcription>

Doctor's Planned Next Steps:
{doctor_next_steps}

Patient Name: {patient_name}
Consultant Name: {consultant_name}
Date: {datetime.now().strftime("%d %B %Y")}

{template_section}

Please draft a professional clinic letter summarizing:
1. The reason for visit
2. History of present illness (from transcription)
3. Examination findings
4. Assessment/clinical impression
5. Plan and next steps (incorporating doctor's input)
6. Follow-up arrangements

Use professional medical language and ensure it is suitable for sending to the patient and/or GP."""
            }
        ]
    )
    return message.content[0].text


def process_consultation(doctor_response: str = None) -> dict:
    """
    Main consultation processing workflow:
    1. Read transcription
    2. Generate prompt for doctor about next steps
    3. If doctor response provided, draft the letter
    """
    # Read transcription
    transcription = read_transcription()
    
    # Generate initial prompt for doctor
    next_steps_prompt = generate_next_steps_prompt(transcription)
    
    result = {
        "transcription": transcription,
        "next_steps_prompt": next_steps_prompt,
        "letter": None
    }
    
    # If doctor has responded with next steps, draft the letter
    if doctor_response:
        letter = draft_letter(transcription, doctor_response)
        result["letter"] = letter
    
    return result
