class AudioPipeline:
    # provider/media_transport get real Protocol types in the next phase.
    def __init__(self, provider: object, media_transport: object) -> None:
        self.provider = provider
        self.media_transport = media_transport

    async def start(self) -> None:
        # Connect provider and media transport
        ...

    async def stop(self) -> None:
        # Stop tasks and clean up resources
        ...
