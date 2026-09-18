from app.voice.contracts import VoiceInput, VoiceOutput

class VoicePipeline:
    """Provider-neutral voice orchestration boundary."""

    def __init__(self, stt=None, tts=None):
        self.stt = stt
        self.tts = tts

    def transcribe(self, request: VoiceInput) -> str:
        if self.stt is None:
            raise RuntimeError("Speech-to-text provider is not configured")
        return self.stt.transcribe(request.audio_path, request.language)

    def synthesize(self, text: str) -> VoiceOutput:
        if self.tts is None:
            return VoiceOutput(text=text)
        return VoiceOutput(text=text, audio_path=self.tts.synthesize(text))
