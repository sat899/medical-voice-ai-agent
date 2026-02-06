"""
Tool: Agentic Actions
Owner: [assign a team member]

Provides tools for planning and executing post-consultation actions
such as drafting letters, ordering tests, and making referrals.
"""

from livekit.agents.llm import function_tool


class ActionTools:
    """Mixin that gives the agent the ability to plan clinical next-steps."""

    @function_tool
    async def draft_letter(self, summary: str, recipient: str) -> str:
        """
        Draft a clinic letter based on the consultation summary.

        Args:
            summary: A short summary of the consultation.
            recipient: Who the letter is addressed to (e.g. GP, specialist).
        """
        # TODO: Implement – generate a letter via LLM with structured template.
        return f"[Placeholder] Letter to {recipient} drafted from summary."

    @function_tool
    async def order_tests(self, tests: str) -> str:
        """
        Order clinical tests for the patient.

        Args:
            tests: Comma-separated list of tests to order (e.g. "FBC, U&E, LFT").
        """
        # TODO: Implement – integrate with lab / EHR ordering system.
        return f"[Placeholder] Ordered tests: {tests}"
