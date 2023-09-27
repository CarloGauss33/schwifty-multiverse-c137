import asyncio
import json
from typing import List, Tuple, Union
from app.models import Character, Location, Episode
from app.jobs.origins_extractor import OriginsExtractor
from app.jobs.char_counter import CharCounter


Classes = Union[Character, Location, Episode]

class Runner:
    def __init__(self, char_tasks: List[Tuple[Classes, str, str]]) -> None:
        self.char_tasks = char_tasks
        self.origins_extractor = OriginsExtractor()
        self.char_counter = CharCounter(char_tasks)

    async def __run(self):
        return await asyncio.gather(
            self.origins_extractor.async_run(),
            self.char_counter.async_run()
        )

    def run(self):
        return json.dumps(
            asyncio.run(self.__run()
        ), indent=4)


if __name__ == "__main__":
    char_count_tasks = [
        (Location, "name", "l"),
        (Episode, "name", "e"),
        (Character, "name", "c"),
    ]

    runner = Runner(char_count_tasks)
    print(runner.run())