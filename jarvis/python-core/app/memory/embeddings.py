import hashlib

class DeterministicEmbedder:
    """Offline embedding placeholder with stable vectors; replace with a real embedding provider."""

    def __init__(self, dimensions: int=128):
        self.dimensions=dimensions

    def embed(self, text: str) -> list[float]:
        values=[0.0]*self.dimensions
        for token in text.lower().split():
            digest=hashlib.sha256(token.encode()).digest()
            index=int.from_bytes(digest[:4],"big") % self.dimensions
            values[index]+=1.0
        return values
