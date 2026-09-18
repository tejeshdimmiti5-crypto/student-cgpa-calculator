from app.agents.base import Agent, AgentResult

class VisionAgent(Agent):
    name="vision"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("screenshot","image","camera","look at"))
    def run(self, command: str) -> AgentResult:
        return AgentResult(self.name,"success",{"status":"vision-agent-ready","command":command},{"requires_vision_runtime":True})
