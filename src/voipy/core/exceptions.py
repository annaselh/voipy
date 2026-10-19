class VoipyError(Exception):
    """Base class for all voipy errors."""


class TelephonyError(VoipyError):
    pass


class ProviderError(VoipyError):
    pass


class AudioError(VoipyError):
    pass


class SessionStateError(VoipyError):
    pass
