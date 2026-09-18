from dataclasses import dataclass, field
import heapq
from itertools import count

@dataclass(order=True)
class ScheduledTask:
    priority: int
    sequence: int
    task_id: str = field(compare=False)
    command: str = field(compare=False)

class PriorityScheduler:
    """Min-heap scheduler. Lower priority number executes first."""

    def __init__(self) -> None:
        self._queue: list[ScheduledTask] = []
        self._sequence = count()

    def submit(self, task_id: str, command: str, priority: int = 100) -> None:
        heapq.heappush(
            self._queue,
            ScheduledTask(priority, next(self._sequence), task_id, command)
        )

    def next_task(self) -> ScheduledTask | None:
        return heapq.heappop(self._queue) if self._queue else None

    def size(self) -> int:
        return len(self._queue)
