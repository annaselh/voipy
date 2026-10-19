from collections.abc import Callable

from .core.interface import TelephonyAdapter, VoiceProvider

ProviderFactory = Callable[[], VoiceProvider]


class Voipy:
    def __init__(self, adapter: TelephonyAdapter, provider_factory: ProviderFactory) -> None:
        self.adapter = adapter
        self.provider_factory = provider_factory
