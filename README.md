# JARVIS AI

A cinematic, modular JARVIS-inspired AI assistant engineered as a real software project.

## 🤖 JARVIS Showcase

This repository is now dedicated to JARVIS. The project brings together a futuristic desktop HUD with a modular AI backend for perception, reasoning, memory, agents, tools, task orchestration and security.

### Core Capabilities

- 🧠 Cognitive core — reasoning, planning, reflection and goal management
- 🤖 Multi-agent runtime — research, coding, testing, browser, vision, computer and tool agents
- 🧩 Tool fabric — calculator, clock, system and file tools with confirmation controls
- 🧠 Memory — working, episodic, temporal and graph memory with retrieval/RAG architecture
- 🗂️ Task engine — DAG planning, dependency tracking and priority scheduling
- 👁️ Vision — image/screenshot integration boundary
- 🎙️ Voice — wake-word, STT/TTS pipeline boundary
- 🌐 Browser — Playwright automation boundary
- 💻 Computer control — action boundary with explicit confirmation for sensitive operations
- 🧪 Code execution — bounded Python execution environment
- 🔐 Security — policy, permissions and audit architecture
- ⚡ Infrastructure — PostgreSQL persistence and Redis queues
- 🖥️ Desktop HUD — React/Vite cinematic command-center interface
- ☕ Java gateway — Spring Boot service foundation
- 🐹 Go workers — concurrent worker foundation

## Architecture

```text
                         ┌─────────────────────┐
                         │       JARVIS        │
                         │   Cognitive Core    │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
               Perception       Reasoning         Memory
                    │               │               │
              Voice / Vision   Planner / LLM   Episodic / Graph
                    └───────────────┬───────────────┘
                                    │
                         ┌──────────▼─────────┐
                         │   Agent Runtime    │
                         └──────────┬─────────┘
                                    │
             ┌──────────┬───────────┼──────────┬──────────┐
             ▼          ▼           ▼          ▼          ▼
          Browser    Computer      Code      Files      APIs
             │          │           │          │          │
             └──────────┴───────────┼──────────┴──────────┘
                                    │
                         ┌──────────▼─────────┐
                         │ Task Graph / Queue │
                         └──────────┬─────────┘
                                    │
                         PostgreSQL + Redis
```

## Repository Structure

```text
jarvis/
├── desktop/       # React/Vite cinematic HUD
├── python-core/   # AI core, agents, memory, tools and orchestration
├── java-gateway/  # Spring Boot gateway
├── go-workers/    # Worker foundation
├── postgres/      # Database schema
├── redis/         # Queue architecture
└── docker-compose.yml
```

## Run JARVIS Core

```bash
cd jarvis
python -m pip install -r python-core/requirements.txt
make cli
```

## Run the API

```bash
cd jarvis
make run
```

Endpoints:

- `GET /health`
- `GET /v1/status`
- `POST /v1/command`
- `WS /v1/ws`

## Launch the JARVIS HUD

```bash
cd jarvis/desktop
npm install
npm run dev
```

## Engineering Principles

- Modular agent architecture
- Event-driven execution
- DSA-based planning and scheduling
- Persistent and contextual memory
- Provider-neutral LLM integration
- Explicit security boundaries
- Safe handling of sensitive operations
- Polyglot services where each language has a defined role

## Security

Sensitive or destructive operations are designed to require explicit confirmation. Secrets and API keys belong in environment variables and must never be committed.

## Project Status

🚧 **Active development** — the architecture and core foundations are in place, with real integrations being built incrementally.

> Inspired by the fictional JARVIS concept from Marvel; this repository focuses on building the underlying real-world software architecture.
