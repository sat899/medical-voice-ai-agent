"""
Tool: Transcription / Scribing
Owner: [assign a team member]

Provides tools for transcribing and summarising consultation audio/text.
"""

import os

from livekit.agents.llm import function_tool

# System prompt for turning a consultation transcript into structured clinical notes.
SCRIBE_SYSTEM_PROMPT = """You are a medical scribe. Your task is to turn a consultation transcript into structured clinical notes.

Rules:
- Use only information that appears in the transcript. Do not add, infer, or invent clinical details.
- Output clear, concise notes suitable for a clinical record.
- Use this structure:
  **Presenting complaint / Reason for attendance**
  **History** (relevant history from the conversation)
  **Examination** (if mentioned)
  **Assessment / Working diagnosis** (only if stated in the transcript; otherwise write "Not documented")
  **Plan** (follow-up, tests, referrals, or advice mentioned)
- If the transcript is very short or unclear, say so and summarise what is there.
- Use neutral, professional language. Do not make diagnoses; only record what was said."""


class ScribeTools:
    """Mixin that gives the agent transcription and summarisation capabilities."""

    @function_tool
    async def summarise_consultation(self, transcript: str) -> str:
        """
        Summarise a consultation transcript into structured clinical notes.

        Args:
            transcript: The raw consultation transcript text.
        """
        transcript = (transcript or "").strip()
        if not transcript:
            return "No transcript was provided. Please provide the consultation transcript to summarise."

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return "Summarisation is not configured (missing OPENAI_API_KEY)."

        try:
            from openai import AsyncOpenAI

            client = AsyncOpenAI(api_key=api_key)
            response = await client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": SCRIBE_SYSTEM_PROMPT},
                    {"role": "user", "content": f"Consultation transcript:\n\n{transcript}"},
                ],
            )
            summary = response.choices[0].message.content
            return summary or "No summary could be generated."
        except Exception as e:
            return f"Summarisation failed: {e!s}"
