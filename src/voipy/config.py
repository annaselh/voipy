from dataclasses import dataclass

@dataclass
class VoipyConfig:
    provider: str = "openai"
    connect_timeout: float = 10.0
    audio_codec: str = "ulaw"