from app.agents.base import Agent, AgentResult

class GeneralAgent(Agent):
    name = "general"

    def can_handle(self, command: str) -> bool:
        return True

    def run(self, command: str) -> AgentResult:
        return AgentResult(
            agent=self.name,
            status="completed",
            output=f"Received task: {command}",
            metadata={"mode": "deterministic"}
        )
