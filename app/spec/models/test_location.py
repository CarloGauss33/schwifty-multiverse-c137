import pytest
from app.models.location import Location

@pytest.fixture
def location_data():
    return {
        'id': 1,
        'name': 'Earth (C-137)',
        'type': 'Planet',
        'dimension': 'Dimension C-137',
        'residents': ['https://rickandmortyapi.com/api/character/1'],
        'url': 'https://rickandmortyapi.com/api/location/1',
        'created': '2017-11-10T12:56:33.798Z'
    }

def test_location_from_dict(location_data):
    location = Location.from_dict(location_data)
    assert location.id == location_data['id']
    assert location.name == location_data['name']
    assert location.type == location_data['type']
    assert location.dimension == location_data['dimension']
    assert location.residents == location_data['residents']
    assert location.url == location_data['url']
    assert location.created == location_data['created']