from dataclasses import dataclass
from enum import StrEnum


class SessionState(StrEnum):
    CREATED = "created"
    CONNECTING = "connecting"
    ACTIVE = "active"
    CLOSED = "closed"
    FAILED = "failed"


@dataclass
class VoiceSession:
    session_id: str
    channel_id: str
    state: SessionState = SessionState.CREATED
