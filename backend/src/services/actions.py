from src.schemas.actions import (
    AgenticActionsRequest,
    AgenticActionsResponse,
    PlannedAction,
)


async def plan_agentic_actions(
    payload: AgenticActionsRequest,
) -> AgenticActionsResponse:
    """
    Placeholder agentic action planner.

    In the real implementation this would:
    - call LLM / tooling to infer next actions
    - interface with downstream systems (EHR, ordering, letters)
    - respect structured schemas and HITL approvals
    """
    actions: list[PlannedAction] = [
        PlannedAction(
            type="draft_letter",
            description="Draft a clinic letter summarizing the consultation.",
            payload={"template": "general_outpatient_summary"},
        ),
        PlannedAction(
            type="order_test",
            description="Order baseline blood tests (placeholder).",
            payload={"tests": ["FBC", "U&E"]},
        ),
    ]

    return AgenticActionsResponse(actions=actions)

