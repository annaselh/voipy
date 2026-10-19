import pytest

import voipy
from voipy.core.exceptions import (
    AudioError,
    ProviderError,
    SessionStateError,
    TelephonyError,
    VoipyError,
)


@pytest.mark.parametrize("exc", [TelephonyError, ProviderError, AudioError, SessionStateError])
def test_errors_share_base_class(exc: type[Exception]) -> None:
    with pytest.raises(VoipyError):
        raise exc("boom")


def test_voipy_can_be_constructed() -> None:
    adapter = object()

    def factory() -> object:
        return object()

    app = voipy.Voipy(adapter=adapter, provider_factory=factory)
    assert app.adapter is adapter
    assert app.provider_factory is factory
