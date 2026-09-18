import hashlib
import os

class DeterministicEmbedder:
    """Stable offline fallback embedder for local development."""
    def __init__(self, dimensions: int = 256):
        self.dimensions = dimensions

    def embed(self, text: str) -> list[float]:
        values = [0.0] * self.dimensions
        for token in text.lower().split():
            digest = hashlib.sha256(token.encode()).digest()
            index = int.from_bytes(digest[:4], "big") % self.dimensions
            values[index] += 1.0
        return values

class EmbeddingProvider:
    """Provider-neutral embedding facade; falls back to deterministic vectors."""
    def __init__(self):
        self.fallback = DeterministicEmbedder()
        self.provider = os.getenv("JARVIS_EMBEDDING_PROVIDER", "local")

    def embed(self, text: str) -> list[float]:
        # A production provider can be plugged in without changing the memory API.
        return self.fallback.embed(text)
