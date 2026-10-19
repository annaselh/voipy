from dataclasses import dataclass
from enum import StrEnum
from .exceptions import SessionStateError

class SessionState(StrEnum):
    CREATED = "created"
    CONNECTING = "connecting"
    ACTIVE = "active"
    CLOSED = "closed"
    FAILED = "failed"

_ALLOWED = {
    SessionState.CREATED: {SessionState.CONNECTING, SessionState.CLOSED},
    SessionState.CONNECTING: {SessionState.ACTIVE, SessionState.FAILED, SessionState.CLOSED},
    SessionState.ACTIVE: {SessionState.CLOSED, SessionState.FAILED},
    SessionState.FAILED: {SessionState.CLOSED},
    SessionState.CLOSED: set(),
}
@dataclass
class VoiceSession:
    session_id: str
    channel_id: str
    state: SessionState = SessionState.CREATED

    def transition(self, new: SessionState) -> None:
        if new not in _ALLOWED[self.state]:
            raise SessionStateError(f"{self.state} -> {new}")
        self.state = new