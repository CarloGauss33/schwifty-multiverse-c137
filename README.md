# Rick and Morty APP

This application fetches data from the [Rick and Morty API](https://rickandmortyapi.com/) and performs the following tasks:

1. **Char counter:**
    - Counts the number of times the letter "l" appears in the names of all `location` (case insensitive).
    - Counts the number of times the letter "e" appears in the names of all `episode` (case insensitive).
    - Counts the number of times the letter "c" appears in the names of all `character` (case insensitive).
    - Measures the total execution time of the program from start to finish.

2. **Episode locations:**
    - For each `episode`, it indicates the number and a list of `location` (`origin`) of all `character` that appeared in that `episode` (without repeating).
    - Measures the total execution time of the program from start to finish.

## Quick Start Guide

This project uses [Poetry](https://python-poetry.org/) for dependency management. To get started, install Poetry and run the following commands:

### Install dependencies

```bash
python -m pip install poetry
poetry install
```

### Run the application

```bash
poetry run python main.py
```

## Testing

The project uses [pytest](https://docs.pytest.org/en/stable/) for testing. To run the tests, run the following command:

```bash
poetry run pytest app
```

## Folder Structure

The project has the following folder structure:

```
.
├── README.md
├── poetry.lock
├── pyproject.toml
├── app
│   ├── __init__.py
│   ├── spec
│   │   ├── __init__.py
│   │   ├── clients/
│   │   ├── models/
│   │   └── jobs/
│   ├── clients
│   │   ├── __init__.py
│   │   ├── base_client.py
│   │   └── rick_and_morty_client.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── character.py
│   │   ├── episode.py
│   │   └── location.py
│   ├── services
│   │   ├── __init__.py
│   │   └── rick_and_morty_service.py
│   └── jobs
│       ├── __init__.py
│       ├── char_counter.py
│       ├── origins_extractor.py
|       ├── time_reporter.py
│       └── char_on_object_counter.py
└── main.py
```

## Contributing

Despite all known laws of aviation, bees should not be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway. Because bees don't care what humans think is impossible.