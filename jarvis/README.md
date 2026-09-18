# JARVIS AI

A real-world, movie-inspired personal AI assistant platform built as a modular cognitive system.

## JARVIS Showcase

**Perception → Reasoning → Memory → Planning → Agents → Tools → Reflection → Recovery**

### What is implemented

- 🧠 Cognitive orchestration with deterministic planning and optional LLM reasoning
- 🤖 Multi-agent runtime for planning, research, coding, testing, validation and tool use
- 🌐 Browser, 👁️ vision and 💻 computer-control integration boundaries
- 🧩 Tool registry with confirmation gates for sensitive operations
- 🧠 Working, episodic, temporal and graph memory
- 🔎 Hybrid retrieval/RAG architecture
- 🗂️ DAG task planning with dependency validation and priority scheduling
- ♻️ Reflection and bounded retry/recovery
- ⚡ Event bus + WebSocket streaming
- 🐘 PostgreSQL persistence and Redis queue foundation
- 🧪 Bounded Python code execution
- 🎙️ Voice wake-word/STT/TTS provider boundary
- 🖥️ React/Vite cinematic desktop HUD
- ☕ Spring Boot Java gateway foundation
- 🐹 Go worker foundation

## Architecture

```text
                         ┌─────────────────────┐
                         │       JARVIS        │
                         │   Cognitive Core    │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              ▼                     ▼                     ▼
        Perception              Reasoning               Memory
       Voice / Vision        LLM / Planner       Episodic / RAG / Graph
              └─────────────────────┬─────────────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │    Task Graph       │
                         │ Priority Scheduler  │
                         └──────────┬──────────┘
                                    ▼
                         ┌─────────────────────┐
                         │   Agent Runtime     │
                         └──────────┬──────────┘
                                    ▼
                Browser • Computer • Code • Files • APIs
                                    │
                         ┌──────────▼──────────┐
                         │ Secure Tool Fabric  │
                         └──────────┬──────────┘
                                    ▼
                         PostgreSQL + Redis
```

## Repository

```text
jarvis/
├── desktop/             # React/Vite cinematic HUD
├── python-core/         # cognition, agents, memory, tools
├── java-gateway/        # Spring Boot control-plane foundation
├── go-workers/          # concurrent worker foundation
├── postgres/             # schema
├── redis/                # queue design
└── docker-compose.yml
```

## Run the Core

```bash
cd jarvis
python -m pip install -r python-core/requirements.txt
PYTHONPATH=python-core python python-core/app/main.py
```

## Run the API

```bash
cd jarvis
PYTHONPATH=python-core uvicorn app.api.server:app --reload --app-dir python-core
```

Endpoints:

- `GET /health`
- `GET /v1/status`
- `POST /v1/command`
- `WS /v1/ws`

## Run the HUD

```bash
cd jarvis/desktop
npm install
npm run dev
```

## Infrastructure

```bash
cd jarvis
docker compose up -d
```

PostgreSQL and Redis are optional for local development because the memory layer is designed to fail soft when external infrastructure is unavailable.

## Security

Sensitive or destructive operations are blocked behind explicit confirmation. API keys belong in environment variables and must never be committed. Computer-control capabilities are intentionally kept behind a security boundary.

## Engineering Stack

| Layer | Technology |
|---|---|
| AI / Agents / DSA | Python |
| Control plane | Java / Spring Boot |
| Desktop interface | TypeScript/React/Vite |
| Workers | Go |
| Native modules | Rust / C++ |
| Data | PostgreSQL / Redis / SQL |
| Browser | Playwright |
| API | FastAPI + WebSocket |
| Deployment foundation | Docker |

## Project Status

**Active development.** The JARVIS cognitive foundation, execution boundary, security gates, memory architecture, task engine, agent runtime, API, HUD and infrastructure foundations are implemented. Provider-specific integrations such as production STT/TTS, vision models, full computer control and distributed workers remain integration work rather than being falsely represented as complete.

> Inspired by the fictional JARVIS concept; this project implements a real software architecture rather than claiming fictional capabilities.
