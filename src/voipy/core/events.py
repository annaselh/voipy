from dataclasses import dataclass


@dataclass
class CallStarted:
    channel_id: str
    caller: str | None = None

@dataclass
class CallEnded:
    channel_id: str
    reason: str | None = None

@dataclass
class SpeechStarted:
    session_id: str