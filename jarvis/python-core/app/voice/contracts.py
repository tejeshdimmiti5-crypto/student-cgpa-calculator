from dataclasses import dataclass

@dataclass
class VoiceInput:
    audio_path: str
    language: str = "en-IN"

@dataclass
class VoiceOutput:
    text: str
    audio_path: str | None = None
