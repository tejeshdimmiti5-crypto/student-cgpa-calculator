from contextlib import contextmanager
from time import perf_counter

class Tracer:
    @contextmanager
    def span(self, name: str):
        start = perf_counter()
        try:
            yield {"name": name}
        finally:
            _ = perf_counter() - start
