"""
Tool: Transcription / Scribing
Owner: [assign a team member]

Provides tools for transcribing and summarising consultation audio/text.
"""

from livekit.agents.llm import function_tool


class ScribeTools:
    """Mixin that gives the agent transcription and summarisation capabilities."""

    @function_tool
    async def summarise_consultation(self, transcript: str) -> str:
        """
        Summarise a consultation transcript into structured clinical notes.

        Args:
            transcript: The raw consultation transcript text.
        """
        # TODO: Implement – call an LLM or use a structured output chain.
        return f"[Placeholder] Summary of {len(transcript)} characters of transcript."
