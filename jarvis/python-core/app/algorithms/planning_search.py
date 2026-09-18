from dataclasses import dataclass
import heapq

@dataclass(order=True)
class SearchState:
    priority: float
    cost: float
    state: str

class BeamPlanner:
    """Bounded best-first search for selecting promising task plans."""
    def __init__(self, beam_width: int = 4):
        self.beam_width=beam_width

    def select(self, candidates: list[tuple[str,float]]) -> list[str]:
        heap=[SearchState(-score,0.0,state) for state,score in candidates]
        heapq.heapify(heap)
        return [heapq.heappop(heap).state for _ in range(min(self.beam_width,len(heap)))]
