from app.perception.models import PerceptionInput, PerceptionResult

class PerceptionEngine:
    """Normalizes incoming modalities before reasoning."""

    def process(self, item: PerceptionInput) -> PerceptionResult:
        text = str(item.content) if item.modality == "text" else None
        return PerceptionResult(
            modality=item.modality,
            normalized_text=text,
            metadata={"source": item.source},
        )
