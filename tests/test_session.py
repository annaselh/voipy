import pytest

from voipy.core.exceptions import SessionStateError
from voipy.core.session import SessionState, VoiceSession


def make() -> VoiceSession:
    return VoiceSession(session_id="s1", channel_id="ch1")


def test_happy_path() -> None:
    s = make()
    s.transition(SessionState.CONNECTING)
    s.transition(SessionState.ACTIVE)
    s.transition(SessionState.CLOSED)
    assert s.state is SessionState.CLOSED


@pytest.mark.parametrize(
    "path",
    [
        [SessionState.ACTIVE],  # skip CONNECTING
        [SessionState.CLOSED, SessionState.CONNECTING],  # reopen after CLOSED
        [SessionState.CONNECTING, SessionState.FAILED, SessionState.ACTIVE],
    ],
)
def test_illegal_transition(path: list[SessionState]) -> None:
    s = make()
    with pytest.raises(SessionStateError):
        for state in path:
            s.transition(state)
