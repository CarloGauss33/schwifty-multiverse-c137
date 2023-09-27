import pytest
from aiohttp import ClientSession
from aioresponses import aioresponses
from app.clients.base_client import BaseClient

@pytest.fixture
def setup_client():
    client = BaseClient('http://baseurl.com')
    yield client

@pytest.mark.asyncio
async def test_init(setup_client):
    assert setup_client.base_url == 'http://baseurl.com'
    assert setup_client.session is None

@pytest.mark.asyncio
async def test_start(setup_client):
    await setup_client.start()
    assert isinstance(setup_client.session, ClientSession)

@pytest.mark.asyncio
async def test_stop(setup_client):
    await setup_client.start()
    await setup_client.stop()
    assert setup_client.session is None

@pytest.mark.asyncio
async def test_get(setup_client):
    async with setup_client as client:
        with aioresponses() as mocked:
            mocked.get('http://baseurl.com/endpoint', payload={'key': 'value'})
            response = await client.get('/endpoint')
            assert response == {'key': 'value'}

@pytest.mark.asyncio
async def test_aenter_aexit(setup_client):
    async with setup_client as client:
        assert isinstance(client.session, ClientSession)
    assert client.session is None