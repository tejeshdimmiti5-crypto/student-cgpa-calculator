from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Any

class WorkerPool:
    """Local concurrent worker abstraction; can later map to Go distributed workers."""

    def __init__(self, max_workers: int = 4) -> None:
        self.pool = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, fn: Callable[..., Any], *args, **kwargs):
        return self.pool.submit(fn, *args, **kwargs)

    def shutdown(self, wait: bool = True) -> None:
        self.pool.shutdown(wait=wait)
