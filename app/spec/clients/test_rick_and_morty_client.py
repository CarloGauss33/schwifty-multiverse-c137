import pytest
from unittest.mock import AsyncMock, patch
from app.clients.rick_and_morty_client import RickAndMortyClient

@pytest.fixture
def client():
    with patch.object(RickAndMortyClient, '_RickAndMortyClient__get') as mocked_get:
        mocked_get.return_value = AsyncMock()
        client = RickAndMortyClient()
        yield RickAndMortyClient()

@pytest.mark.asyncio
async def test_list_characters(client):
    await client.list_characters()
    client._RickAndMortyClient__get.assert_called_once_with(
        'api/character',
        params=None
    )

@pytest.mark.asyncio
async def test_list_locations(client):
    await client.list_locations()
    client._RickAndMortyClient__get.assert_called_once_with(
        'api/location',
        params=None
    )

@pytest.mark.asyncio
async def test_list_episodes(client):
    await client.list_episodes()
    client._RickAndMortyClient__get.assert_called_once_with(
        'api/episode',
        params=None
    )

@pytest.mark.asyncio
async def test_get_character(client):
    await client.get_character(1)
    client._RickAndMortyClient__get.assert_called_once_with(
        'api/character/1'
    )

@pytest.mark.asyncio
async def test_get_location(client):
    await client.get_location(1)
    client._RickAndMortyClient__get.assert_called_once_with(
        'api/location/1'
    )

@pytest.mark.asyncio
async def test_get_episode(client):
    await client.get_episode(1)
    client._RickAndMortyClient__get.assert_called_once_with(
        'api/episode/1'
    )
