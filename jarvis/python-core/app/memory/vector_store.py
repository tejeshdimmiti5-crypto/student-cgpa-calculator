from dataclasses import dataclass
import math
from typing import Any

@dataclass
class VectorMemory:
    key: str
    text: str
    vector: list[float]
    metadata: dict[str, Any]

class InMemoryVectorStore:
    """Vector-store contract. Production embeddings/database can replace this implementation."""

    def __init__(self):
        self.items: list[VectorMemory] = []

    def add(self, key: str, text: str, vector: list[float], **metadata):
        self.items.append(VectorMemory(key, text, vector, metadata))

    @staticmethod
    def cosine(a: list[float], b: list[float]) -> float:
        if not a or not b or len(a) != len(b):
            return 0.0
        dot=sum(x*y for x,y in zip(a,b))
        na=math.sqrt(sum(x*x for x in a))
        nb=math.sqrt(sum(x*x for x in b))
        return dot/(na*nb) if na and nb else 0.0

    def search(self, vector: list[float], limit: int=5):
        ranked=sorted(((self.cosine(vector,x.vector),x) for x in self.items), key=lambda z:z[0], reverse=True)
        return [{"score":round(score,4),"key":item.key,"text":item.text,"metadata":item.metadata} for score,item in ranked[:limit]]
