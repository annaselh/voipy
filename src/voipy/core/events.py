from dataclasses import dataclass

class CallEvent:
    pass

@dataclass
class CallStarted(CallEvent):
    channel_id: str
    caller: str | None = None

@dataclass
class CallEnded(CallEvent):
    channel_id: str
    reason: str | None = None

@dataclass
class DtmfReceived(CallEvent):
    channel_id: str
    digit: str

class ProviderEvent:
    pass

@dataclass
class SpeechStarted(ProviderEvent):
    session_id: str
