# Medical Voice AI Agent

Post-consultation scribe, research, and action support (STT, TTS clarifications, agentic actions). FastAPI backend, Postgres, simple static frontend.

## Run

```bash
docker compose up --build
```

- **API**: http://localhost:8000  
- **Docs**: http://localhost:8000/docs  
- **Frontend**: http://localhost:3000  

## Project structure

| Path | Purpose |
|------|--------|
| `backend/src/main.py` | FastAPI app entry; mounts routers under `/api` |
| `backend/src/api/` | HTTP routes (v1: health, stt, tts, actions, agent) |
| `backend/src/schemas/` | Pydantic request/response models |
| `backend/src/services/` | STT, TTS, actions logic (implement here) |
| `backend/src/agents/` | Orchestration (orchestrator calls services) |
| `backend/src/core/` | Config, shared utilities |
| `frontend/` | Static UI (index.html, main.js); replace with SPA if needed |

## Where to put code

- **New API endpoints** → `backend/src/api/v1/` + schema in `backend/src/schemas/`
- **STT / transcription** → `backend/src/services/stt.py`
- **Clarification questions (TTS)** → `backend/src/services/tts.py`
- **Agentic actions (letters, tests, etc.)** → `backend/src/services/actions.py`
- **Orchestration / flow** → `backend/src/agents/orchestrator.py`
- **Frontend** → `frontend/` (keep calling the same `/api/v1/*` endpoints)

## Contributing

1. Pick a module (e.g. services, agents, api, frontend).
2. Add or change code in the relevant folder; keep request/response contracts in `schemas/` so others can rely on them.
3. Run with `docker compose up --build` and test via http://localhost:8000/docs or the frontend at http://localhost:3000.
