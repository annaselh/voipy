from .interface import MediaTransport, VoiceProvider


class AudioPipeline:
    # provider/media_transport get real Protocol types in the next phase.
    def __init__(self, provider: VoiceProvider, transport: MediaTransport) -> None:
        self.provider = provider
        self.transport = transport

    async def start(self) -> None:
        # Connect provider and media transport
        ...

    async def stop(self) -> None:
        # Stop tasks and clean up resources
        ...
