from app.agents.base import Agent, AgentResult

class ComputerAgent(Agent):
    name="computer"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("click","type","keyboard","mouse","desktop"))
    def run(self, command: str) -> AgentResult:
        return AgentResult(self.name,"success",{"status":"computer-agent-ready","command":command},{"requires_confirmation_for_actions":True})
