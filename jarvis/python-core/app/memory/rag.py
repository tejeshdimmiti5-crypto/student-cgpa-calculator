class RAGContext:
    """Hybrid RAG facade over the vector store with optional reranking."""
    def __init__(self, embedder, store, reranker=None):
        self.embedder=embedder
        self.store=store
        self.reranker=reranker

    def retrieve(self, query: str, limit: int=5):
        vector=self.embedder.embed(query)
        results=self.store.search(vector, max(limit,10))
        if self.reranker:
            results=self.reranker(results, query)
        return results[:limit]

    def build_prompt_context(self, query: str, limit: int=5) -> str:
        results=self.retrieve(query,limit)
        return "\n".join(f"[{r.get('score',0)}] {r.get('text','')}" for r in results)
