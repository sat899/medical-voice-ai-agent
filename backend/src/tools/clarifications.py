"""
Tool: Clarification Questions
Owner: [assign a team member]

Provides tools for generating and managing structured clarification questions
that the agent can ask the consultant during or after a consultation.
"""

import os

from livekit.agents.llm import function_tool

# System prompt for generating context-aware clarification questions for the clinician.
CLARIFICATION_SYSTEM_PROMPT = """You are a medical assistant helping to capture clear clinical information. Your task is to suggest brief clarification questions that a clinician could be asked after or during a consultation, based on the consultation text provided.

Rules:
- Generate 3 to 5 short, relevant questions. Only suggest questions that are appropriate given what is already in the consultation text (e.g. gaps, ambiguities, or important follow-ups).
- Questions should be concise and suitable for voice – the agent will read them aloud.
- Focus on: working diagnosis, red-flag symptoms, uncertainties, medication or allergy clarification, follow-up plans, or key history that seems missing.
- Do not invent clinical details. Do not ask questions that are already clearly answered in the text.
- Output a simple numbered list of questions, one per line. No preamble or explanation unless the text is empty or too short to suggest questions."""


class ClarificationTools:
    """Mixin that gives the agent the ability to ask structured follow-up questions."""

    @function_tool
    async def suggest_clarifications(self, consultation_text: str) -> str:
        """
        Analyse consultation text and suggest clarification questions for the clinician.

        Args:
            consultation_text: The consultation transcript or notes so far.
        """
        consultation_text = (consultation_text or "").strip()
        if not consultation_text:
            return "No consultation text was provided. Please provide the transcript or notes so far to suggest clarification questions."

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return "Clarification suggestions are not configured (missing OPENAI_API_KEY)."

        try:
            from openai import AsyncOpenAI

            client = AsyncOpenAI(api_key=api_key)
            response = await client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": CLARIFICATION_SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"Consultation text or notes:\n\n{consultation_text}",
                    },
                ],
            )
            questions = response.choices[0].message.content
            return questions or "No clarification questions could be generated."
        except Exception as e:
            return f"Suggesting clarifications failed: {e!s}"
