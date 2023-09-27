import asyncio
from app.services.rick_and_morty_service import RickAndMortyService
from app.jobs.time_reporter import TimeReporter

class OriginsExtractor:
    def __init__(self) -> None:
        self.service = RickAndMortyService()
        self.dict_result = {
            "exercise_name": "Origins extractor",
            "time": None,
            "in_time": None,
            "results": []
        }

    async def __run_episode_location_counter(self, episode):
        episode_characters = episode.characters
        characters = await self.service.get_multiple_characters_by_id(
            [character.id for character in episode_characters]
        )

        origins = set([character.origin.name for character in characters])

        self.dict_result["results"].append({
            "name": episode.name,
            "episode": episode.episode,
            "locations_quantity": len(origins),
            "locations": list(origins)
        })

    async def __run_location_counter(self):
        episodes = await self.service.get_episodes()

        await asyncio.gather(
            *[self.__run_episode_location_counter(episode) for episode in episodes]
        )

    async def async_run(self):
        timer = TimeReporter()

        await self.__run_location_counter()

        timer.stop()
        self.dict_result["time"] = timer.report()
        self.dict_result["in_time"] = timer.in_time()

        return self.dict_result

    def run(self):
        return asyncio.run(self.async_run())