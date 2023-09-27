from typing import List

class Episode:
    class Character:
        def __init__(self, url: str) -> None:
            self.id = url.split('/')[-1]

    def __init__(
        self,
        id: int,
        name: str,
        air_date: str,
        episode: str,
        characters: List[Character],
        url: str,
        created: str
    ) -> None:
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            air_date=data['air_date'],
            episode=data['episode'],
            characters=[Episode.Character(url) for url in data['characters']],
            url=data['url'],
            created=data['created']
        )

    def __repr__(self) -> str:
        return f'<Episode {self.id}>'