from app.config import Settings
from app.queue.redis_queue import RedisQueue

class TaskQueue:
    """Priority-aware Redis queue facade."""

    QUEUES = {
        "high": "jarvis:tasks:high",
        "normal": "jarvis:tasks:normal",
        "low": "jarvis:tasks:low",
    }

    def __init__(self, redis_url: str | None = None) -> None:
        self.redis = RedisQueue(redis_url or Settings().redis_url)

    def enqueue(self, payload: dict, priority: str = "normal") -> None:
        queue = self.QUEUES.get(priority, self.QUEUES["normal"])
        self.redis.enqueue(queue, payload)

    def dequeue(self, priority: str = "high", timeout: int = 5):
        queue = self.QUEUES.get(priority, self.QUEUES["high"])
        return self.redis.dequeue(queue, timeout)
