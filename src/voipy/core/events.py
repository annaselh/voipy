import time
from dataclasses import dataclass, field
from typing import Literal

from .audio import AudioFrame


@dataclass(frozen=True, kw_only=True)
class Event:
    timestamp: float = field(default_factory=time.monotonic)


@dataclass(frozen=True)
class CallEvent(Event):
    channel_id: str


@dataclass(frozen=True)
class CallStarted(CallEvent):
    caller: str | None = None


@dataclass(frozen=True)
class CallEnded(CallEvent):
    reason: str | None = None


@dataclass(frozen=True)
class DtmfReceived(CallEvent):
    digit: str


@dataclass(frozen=True)
class ProviderEvent(Event):
    pass


@dataclass(frozen=True)
class AudioOut(ProviderEvent):
    frame: AudioFrame


@dataclass(frozen=True)
class SpeechStarted(ProviderEvent):
    pass


@dataclass(frozen=True)
class SpeechStopped(ProviderEvent):
    pass


@dataclass(frozen=True)
class Transcript(ProviderEvent):
    text: str
    role: Literal["user", "assistant"]
    final: bool


@dataclass(frozen=True)
class ProviderFailed(ProviderEvent):
    error: Exception
