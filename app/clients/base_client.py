from aiohttp import ClientSession

class BaseClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.session = None

    async def stop(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def start(self):
        if not self.session:
            self.session = ClientSession()

    async def get(self, endpoint: str, params: dict = None) -> dict:
        async with self.session.get(
            f"{self.base_url}{endpoint}", params=params
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def __aexit__(self, exc_type, exc, tb):
        await self.stop()

    async def __aenter__(self):
        await self.start()
        return self