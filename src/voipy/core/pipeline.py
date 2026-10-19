class AudioPipeline:
    def __init__(self, provider, media_transport):
        self.provider = provider
        self.media_transport = media_transport

    async def start(self):
        # Connect provider and media transport
        ...

    async def stop(self):
        #Stop task and clean resources
        ...