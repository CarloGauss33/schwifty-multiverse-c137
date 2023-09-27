import pytest
from app.models.character import Character

@pytest.fixture
def character_data():
    return {
        'id': 1,
        'name': 'Rick Sanchez',
        'status': 'Alive',
        'species': 'Human',
        'type': '',
        'gender': 'Male',
        'origin': {'name': 'Earth (C-137)', 'url': 'https://rickandmortyapi.com/api/location/1'},
        'location': {'name': 'Earth (Replacement Dimension)', 'url': 'https://rickandmortyapi.com/api/location/20'},
        'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg',
        'episode': ['https://rickandmortyapi.com/api/episode/1'],
        'url': 'https://rickandmortyapi.com/api/character/1',
        'created': '2017-11-04T18:48:46.250Z'
    }

def test_character_from_dict(character_data):
    character = Character.from_dict(character_data)
    assert character.id == character_data['id']
    assert character.name == character_data['name']
    assert character.status == character_data['status']
    assert character.species == character_data['species']
    assert character.type == character_data['type']
    assert character.gender == character_data['gender']
    assert character.origin.name == character_data['origin']['name']
    assert character.origin.url == character_data['origin']['url']
    assert character.location.name == character_data['location']['name']
    assert character.location.url == character_data['location']['url']
    assert character.image == character_data['image']
    assert character.episode == character_data['episode']
    assert character.url == character_data['url']
    assert character.created == character_data['created']