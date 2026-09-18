class RAGContext:
    def __init__(self, embedder, store):
        self.embedder=embedder
        self.store=store

    def retrieve(self, query: str, limit: int=5):
        vector=self.embedder.embed(query)
        return self.store.search(vector, limit)

    def build_prompt_context(self, query: str, limit: int=5) -> str:
        results=self.retrieve(query, limit)
        return "\n".join(f"[{r['score']}] {r['text']}" for r in results)
