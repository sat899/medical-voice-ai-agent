"""
Tool: Clarification Questions
Owner: [assign a team member]

Provides tools for generating and managing structured clarification questions
that the agent can ask the consultant during or after a consultation.
"""

from livekit.agents.llm import function_tool


class ClarificationTools:
    """Mixin that gives the agent the ability to ask structured follow-up questions."""

    @function_tool
    async def suggest_clarifications(self, consultation_text: str) -> str:
        """
        Analyse consultation text and suggest clarification questions for the clinician.

        Args:
            consultation_text: The consultation transcript or notes so far.
        """
        # TODO: Implement – e.g. use existing questionnaire templates,
        #       call an LLM to generate context-specific questions.
        return (
            "[Placeholder] Suggested questions:\n"
            "1. What is your working diagnosis?\n"
            "2. Are there any red-flag symptoms you are concerned about?"
        )
