from typing import Union, List
from app.models import Character, Location, Episode

class CharsOnObjectCounter:
    def __init__(self, char: str, target_attribute: str) -> None:
        self.char = char.lower()
        self.target_attribute = target_attribute
        self.count = 0

    def _add_multiple(self, obj: List[Union[Character, Location, Episode]]) -> None:
        self.count += sum([
            getattr(o, self.target_attribute).lower().count(self.char) for o in obj
        ])

    def add(self, obj: Union[Character, Location, Episode]) -> None:
        self.count += getattr(obj, self.target_attribute).lower().count(self.char)

    def result(self) -> int:
        return self.count