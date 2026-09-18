from app.agents.base import Agent, AgentResult

class BrowserAgent(Agent):
    name="browser"
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("open website","browse","web page","url"))
    def run(self, command: str) -> AgentResult:
        return AgentResult(self.name,"success",{"status":"browser-agent-ready","command":command},{"requires_browser_runtime":True})
