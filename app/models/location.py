class Location:
    def __init__(
        self,
        id: int,
        name: str,
        type: str,
        dimension: str,
        residents: list,
        url: str,
        created: str
    ) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.dimension = dimension
        self.residents = residents
        self.url = url
        self.created = created

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            type=data['type'],
            dimension=data['dimension'],
            residents=data['residents'],
            url=data['url'],
            created=data['created']
        )

    def __repr__(self) -> str:
        return f'<Location {self.id}>'