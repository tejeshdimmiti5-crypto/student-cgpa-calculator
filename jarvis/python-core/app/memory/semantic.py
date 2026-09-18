from app.memory.embeddings import EmbeddingProvider
from app.memory.vector_store import InMemoryVectorStore
from app.memory.reranker import rerank

class SemanticMemory:
    """Unified semantic memory facade with embedding, vector search and reranking."""
    def __init__(self):
        self.embedder = EmbeddingProvider()
        self.store = InMemoryVectorStore()

    def remember(self, key: str, text: str, **metadata):
        self.store.add(key, text, self.embedder.embed(text), **metadata)

    def recall(self, query: str, limit: int = 5):
        results = self.store.search(self.embedder.embed(query), max(limit, 10))
        return rerank(results, query)[:limit]
