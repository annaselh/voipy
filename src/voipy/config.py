from dataclasses import dataclass

from .core.audio import AudioCodec


@dataclass
class VoipyConfig:
    connect_timeout: float = 10.0
    audio_codec: str = AudioCodec.ULAW
    sample_rate: int = 8000
