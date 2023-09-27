import asyncio
from app.clients.rick_and_morty_client import RickAndMortyClient
from app.models import Character, Location, Episode

class RickAndMortyService:
    def __init__(self) -> None:
        self.client = RickAndMortyClient()

    async def get_multiple_characters_by_id(self, ids: list) -> list:
        response = await self.client.get_character(','.join(ids))

        characters = [Character.from_dict(character) for character in response]

        return characters

    async def get_multiple_locations_by_id(self, ids: list) -> list:
        response = await self.client.get_location(','.join(ids))

        locations = [Location.from_dict(location) for location in response]

        return locations

    async def get_multiple_episodes_by_id(self, ids: list) -> list:
        response = await self.client.get_episode(','.join(ids))

        episodes = [Episode.from_dict(episode) for episode in response]

        return episodes

    async def get_characters_for_page(self, page: int) -> list:
        response = await self.client.list_characters(params={'page': page})

        characters = [
            Character.from_dict(character) for character in response['results']
        ]

        return characters

    async def get_locations_for_page(self, page: int) -> list:
        response = await self.client.list_locations(params={'page': page})

        locations = [Location.from_dict(location) for location in response['results']]

        return locations

    async def get_episodes_for_page(self, page: int) -> list:
        response = await self.client.list_episodes(params={'page': page})

        episodes = [Episode.from_dict(episode) for episode in response['results']]

        return episodes

    async def load_pages(self, func, pages_count):
        pages = [func(page) for page in range(1, pages_count + 1)]

        return sum(await asyncio.gather(*pages), [])

    async def get_number_of_pages_for_resource(self, resource: str) -> int:
        response = await getattr(self.client, f'list_{resource}s')()

        return response['info']['pages']

    async def get_characters(self) -> list:
        return await self.load_pages(
            self.get_characters_for_page,
            await self.get_number_of_pages_for_resource('character')
        )

    async def get_locations(self) -> list:
        return await self.load_pages(
            self.get_locations_for_page,
            await self.get_number_of_pages_for_resource('location')
        )

    async def get_episodes(self) -> list:
        return await self.load_pages(
            self.get_episodes_for_page,
            await self.get_number_of_pages_for_resource('episode')
        )