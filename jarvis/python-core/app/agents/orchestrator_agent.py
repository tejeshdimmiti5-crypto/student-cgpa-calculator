from app.agents.base import Agent, AgentResult

class OrchestratorAgent(Agent):
    """Coordinates multi-agent tasks without bypassing the central execution boundary."""
    name = "orchestrator"

    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("multiple agents", "coordinate", "orchestrate", "complex task"))

    def run(self, command: str) -> AgentResult:
        return AgentResult(
            self.name,
            "success",
            {
                "status": "delegation-planned",
                "command": command,
                "next": "central-orchestrator",
            },
            {"safe_boundary": True},
        )
