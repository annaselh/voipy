import pytest

import voipy
from voipy.core.exceptions import (
    AudioError,
    ProviderError,
    SessionStateError,
    TelephonyError,
    VoipyError,
)


def test_voipy_can_be_constructed() -> None:
    assert isinstance(voipy.Voipy(), voipy.Voipy)


@pytest.mark.parametrize("exc", [TelephonyError, ProviderError, AudioError, SessionStateError])
def test_errors_share_base_class(exc: type[Exception]) -> None:
    with pytest.raises(VoipyError):
        raise exc("boom")
