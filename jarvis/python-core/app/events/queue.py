from queue import Queue
from typing import Any

class EventQueue:
    """In-process event queue abstraction for a future Redis/message-bus backend."""

    def __init__(self) -> None:
        self.queue: Queue[Any] = Queue()

    def put(self, event: Any) -> None:
        self.queue.put(event)

    def get(self, timeout: float | None = None) -> Any:
        return self.queue.get(timeout=timeout)
