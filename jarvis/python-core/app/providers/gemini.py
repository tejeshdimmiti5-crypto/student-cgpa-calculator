import json
import os
from app.providers.base import LLMProvider
from app.reasoning.models import ReasoningRequest, ReasoningPlan

class GeminiProvider(LLMProvider):
    """Google GenAI adapter using a current stable Gemini model."""
    name = "gemini"
    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("JARVIS_LLM_MODEL", "gemini-2.0-flash")
        self.api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self._client = None
    def _get_client(self):
        if not self.api_key: return None
        if self._client is None:
            from google import genai
            self._client = genai.Client(api_key=self.api_key)
        return self._client
    def plan(self, request: ReasoningRequest) -> ReasoningPlan:
        client = self._get_client()
        if client is None: raise RuntimeError("Gemini API key is not configured")
        prompt=("You are JARVIS, a structured planning engine. Return ONLY valid JSON with keys goal, steps, confidence, metadata. "
                "steps must be a JSON array of concise executable planning steps. confidence must be a number from 0 to 1.\n\n"
                f"Goal: {request.command}\nContext: {json.dumps(request.context, default=str)}")
        response=client.models.generate_content(model=self.model, contents=prompt)
        data=json.loads(getattr(response,"text","") or "")
        return ReasoningPlan(goal=str(data.get("goal",request.command)),
            steps=[str(x) for x in data.get("steps",[])],
            confidence=max(0.0,min(1.0,float(data.get("confidence",0.5)))),
            metadata={"provider":self.name,"model":self.model,**dict(data.get("metadata",{}))})
