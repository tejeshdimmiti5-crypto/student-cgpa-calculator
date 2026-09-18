from app.messaging.broker import AgentBroker
from app.messaging.protocol import AgentEnvelope, AgentMessage

class AgentManager:
    def __init__(self, runtime):
        self.runtime=runtime
        self.broker=AgentBroker()

    def delegate(self, sender: str, recipient: str, command: str, correlation_id: str=""):
        self.broker.send(AgentEnvelope(AgentMessage(sender,recipient,"task",{"command":command},correlation_id)))

    def process_one(self, agent: str):
        envelope=self.broker.receive(agent)
        if not envelope:
            return None
        command=envelope.message.payload["command"]
        return self.runtime.execute(command, preferred=agent)
