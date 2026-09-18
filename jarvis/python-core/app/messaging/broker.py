from collections import defaultdict, deque
from app.messaging.protocol import AgentEnvelope

class AgentBroker:
    """In-process agent message broker; Redis/NATS can replace it for distributed deployment."""

    def __init__(self):
        self.queues=defaultdict(deque)

    def send(self, envelope: AgentEnvelope):
        self.queues[envelope.message.recipient].append(envelope)

    def receive(self, agent: str):
        return self.queues[agent].popleft() if self.queues[agent] else None
