from clients.base_client import BaseClient

class RickAndMortyClient:
    BASE_URL = 'https://rickandmortyapi.com/'

    async def __get(self, path, params=None):
        async with BaseClient(self.BASE_URL) as client:
            return await client.get(path, params=params)

    async def list_characters(self, params=None) -> dict:
        return await self.__get('api/character', params=params)

    async def list_locations(self, params=None) -> dict:
        return await self.__get('api/location', params=params)

    async def list_episodes(self, params=None) -> dict:
        return await self.__get('api/episode', params=params)

    async def get_character(self, character_id: int) -> dict:
        return await self.__get(f'api/character/{character_id}')

    async def get_location(self, location_id: int) -> dict:
        return await self.__get(f'api/location/{location_id}')

    async def get_episode(self, episode_id: int) -> dict:
        return await self.__get(f'api/episode/{episode_id}')