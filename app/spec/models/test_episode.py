import pytest
from app.models.episode import Episode

@pytest.fixture
def episode_data():
    return {
        'id': 1,
        'name': 'Pilot',
        'air_date': 'December 2, 2013',
        'episode': 'S01E01',
        'characters': ['https://rickandmortyapi.com/api/character/1'],
        'url': 'https://rickandmortyapi.com/api/episode/1',
        'created': '2017-11-10T12:56:33.798Z'
    }

def test_episode_from_dict(episode_data):
    episode = Episode.from_dict(episode_data)
    assert episode.id == episode_data['id']
    assert episode.name == episode_data['name']
    assert episode.air_date == episode_data['air_date']
    assert episode.episode == episode_data['episode']
    assert episode.characters[0].id == '1'
    assert episode.url == episode_data['url']
    assert episode.created == episode_data['created']