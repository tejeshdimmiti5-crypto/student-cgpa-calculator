import json

class RedisQueue:
    """Redis-backed task queue abstraction."""

    def __init__(self, url: str):
        self.url = url
        self.client = None

    def connect(self):
        import redis
        self.client = redis.from_url(self.url, decode_responses=True)
        return self.client

    def enqueue(self, queue: str, payload: dict) -> None:
        if self.client is None:
            self.connect()
        self.client.rpush(queue, json.dumps(payload))

    def dequeue(self, queue: str, timeout: int = 5) -> dict | None:
        if self.client is None:
            self.connect()
        item = self.client.blpop(queue, timeout=timeout)
        return json.loads(item[1]) if item else None
