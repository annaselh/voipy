from dataclasses import dataclass
from enum import Enum

class AudioCodec(str, Enum):
    ULAW = "ulaw"
    ALAW = "alaw"
    PCM16 = "pcm16"

@dataclass(frozen=True, slots=True)
class AudioFrame:
    data: bytes
    codec: AudioCodec = AudioCodec.ULAW
    sample_rate: int = 8000
