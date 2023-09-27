import asyncio
from typing import List, Tuple, Union
from app.services.rick_and_morty_service import RickAndMortyService
from app.jobs.chars_on_object_counter import CharsOnObjectCounter
from app.jobs.time_reporter import TimeReporter
from app.models import Character, Location, Episode

Classes = Union[Character, Location, Episode]

class CharCounter:
    objects_iterators = {
        Character: RickAndMortyService().get_characters,
        Location: RickAndMortyService().get_locations,
        Episode: RickAndMortyService().get_episodes
    }

    def __init__(self, char_tasks: List[Tuple[Classes, str, str]]) -> None:
        self.char_tasks = char_tasks
        self._result_dict = {
            "exercise_name": "Char counter",
            "time": None,
            "in_time": None,
            "results": []
        }

    async def __run_char_counter(self, task):
        object_class, attribute, char = task

        counter = CharsOnObjectCounter(char, attribute)
        counter._add_multiple(await self.objects_iterators[object_class]())

        self._result_dict["results"].append({
            "char": char,
            "count": counter.result(),
            "resource": object_class.__name__.lower(),
        })

    async def _run_char_tasks(self):
        await asyncio.gather(
            *[self.__run_char_counter(task) for task in self.char_tasks]
        )

    async def async_run(self):
        timer = TimeReporter()

        await self._run_char_tasks()

        timer.stop()
        self._result_dict["time"] = timer.report()
        self._result_dict["in_time"] = timer.in_time()

        return self._result_dict

    def run(self):
        return asyncio.run(self.async_run())
