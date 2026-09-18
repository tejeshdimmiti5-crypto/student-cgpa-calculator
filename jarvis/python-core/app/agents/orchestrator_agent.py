from app.agents.base import Agent, AgentResult

class OrchestratorAgent(Agent):
    name = "orchestrator"

    def can_handle(self, command: str) -> bool:
        return True

    def run(self, command: str) -> AgentResult:
        return AgentResult(
            agent=self.name,
            status="success",
            output={"mode": "multi-agent", "goal": command},
            metadata={"delegation": True},
        )
