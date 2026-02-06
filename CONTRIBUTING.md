# Contributing – Task Breakdown

Each tool file in `backend/src/tools/` is designed to be owned by one person.
Pick a file, implement the `TODO`s, and submit a PR. You should rarely need to
edit anyone else's file.

---

## File Ownership & Tasks

### `tools/notes.py` – Clinical Notes

| Task | Description |
|------|-------------|
| Persist notes | Replace the in-memory `dict` with a database (e.g. Postgres, Supabase) |
| Per-session storage | Scope notes to a consultation/session ID instead of a global dict |
| Search notes | Add a `search_notes(query)` tool so the agent can find relevant past notes |

---

### `tools/scribe.py` – Transcription / Scribing

| Task | Description |
|------|-------------|
| Implement `summarise_consultation` | Call an LLM to turn raw transcript text into structured clinical notes |
| Add translation | Add a `translate_transcript(text, target_language)` tool |
| Template support | Generate notes in specific formats (SOAP, clinical letter, discharge summary) |

---

### `tools/clarifications.py` – Clarification Questions

| Task | Description |
|------|-------------|
| Implement `suggest_clarifications` | Use LLM + existing questionnaire templates to generate context-aware questions |
| Speciality-specific questions | Load different question sets per speciality (cardiology, ortho, etc.) |
| Track answers | Add a `record_answer(question_id, answer)` tool so the agent can log clinician responses |

---

### `tools/actions.py` – Agentic Actions (Letters, Tests, Referrals)

| Task | Description |
|------|-------------|
| Implement `draft_letter` | Generate a clinic letter via LLM using a structured template |
| Implement `order_tests` | Integrate with a lab/EHR ordering API or create a structured output |
| Add referrals | Add a `make_referral(speciality, reason)` tool |
| HITL approval | Return a draft for human review before finalising any action |

---

### `tools/appointments.py` – Scheduling & Waiting List

| Task | Description |
|------|-------------|
| Implement `check_availability` | Query a scheduling API or database for open slots |
| Implement `schedule_followup` | Create a booking in the scheduling system |
| Waiting list logic | Add a `add_to_waiting_list(patient_id, priority)` tool with triage logic |
| Cancellation handling | Add a tool to cancel or reschedule appointments |

---

### `prompts.py` – System Prompt

| Task | Description |
|------|-------------|
| Refine instructions | Tune the persona, tone, and boundaries as features are added |
| Speciality modes | Create variants of the prompt for different clinical contexts |

---

### `agent.py` – Agent Entrypoint

| Task | Description |
|------|-------------|
| Add/remove mixins | When a new tool file is ready, import it and add the mixin to the class |
| Agent config | Tune the LLM model, voice, or noise cancellation settings |

You should **not** put tool logic in this file – keep it in `tools/`.

---

## How to Add a New Feature

1. Create a new file in `backend/src/tools/`, e.g. `tools/my_feature.py`.
2. Define a mixin class with `@function_tool` methods.
3. Import it in `agent.py` and add it to `MedicalVoiceAgent`'s base classes.
4. Update `prompts.py` to mention the new capabilities.
5. Test by running `docker compose up --build`.

## Running Locally

```bash
docker compose up --build
```

- **Backend API**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000
- **Voice agent** connects to LiveKit Cloud automatically.
