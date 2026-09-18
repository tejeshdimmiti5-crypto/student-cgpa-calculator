# JARVIS Voice Layer

Architecture:
1. Wake-word detector
2. Speech-to-text provider
3. Cognitive gateway
4. Text-to-speech provider
5. Audio output

The voice layer is intentionally provider-agnostic so local or hosted STT/TTS engines can be selected later.