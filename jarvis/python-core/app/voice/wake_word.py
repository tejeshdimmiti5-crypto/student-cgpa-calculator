class WakeWordDetector:
    def __init__(self, phrase: str = "hey jarvis"):
        self.phrase = phrase.lower()

    def detect(self, text: str) -> bool:
        return self.phrase in text.lower()
