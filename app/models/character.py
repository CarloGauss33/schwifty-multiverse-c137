class Character:
    class Location:
        def __init__(self, name: str, url: str):
            self.name = name
            self.url = url

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                name=data['name'],
                url=data['url']
            )

    class Origin:
        def __init__(self, name: str, url: str):
            self.name = name
            self.url = url

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                name=data['name'],
                url=data['url']
            )


    def __init__(
        self,
        id: id,
        name: str,
        status: str,
        species: str,
        type: str,
        gender: str,
        origin: Origin,
        location: Location,
        image: str,
        episode: list,
        url: str,
        created: str
    ) -> None:
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            status=data['status'],
            species=data['species'],
            type=data['type'],
            gender=data['gender'],
            origin=Character.Origin.from_dict(data['origin']),
            location=Character.Location.from_dict(data['location']),
            image=data['image'],
            episode=data['episode'],
            url=data['url'],
            created=data['created']
        )

    def __repr__(self) -> str:
        return f'<Episode {self.id}>'
