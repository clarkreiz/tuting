# Tutor Accounting Bot

[Читать на русском](README.ru.md)

A bookkeeping project designed for tutors and private educators. The frontend is built using Python, leveraging Telegram for user interaction and the `aiogram` library. The backend will be developed separately in a different repository will be here [backend](https://github.com/clarkreiz/tuting_backend/tree/main)

## TODO List

### Completed:
- ~~Boilerplate with Poetry, mypy, black~~
- ~~Basic CI/CD, Dockerfile~~
- ~~Bot initialization, welcome command~~
- ~~Feature for adding a student~~

### Planned:
- View all students (separate FSM)
- Add payment for a specific student (separate FSM)
- Docker-compose, integration auto-tests for the aiohttp client (stub/mock go server)
- Deploy to production

## Overview

This repository contains the code for the Telegram bot. The bot uses an `aiohttp` client to send and receive messages from the backend.

## Features

- **User-friendly Telegram interface**: Interact with the bot via Telegram.
- **FSM**: Efficiently handle dialogues.
- **Async communication**: Uses `aiohttp` for non-blocking requests to the backend.

## Tools and Dependencies

- **Package Management**: [Poetry](https://python-poetry.org/) is used for dependency management and packaging.
- **Linting and Formatting**: [Ruff](https://github.com/charliermarsh/ruff) is chosen as the linter and formatter. Previously, I used `flake8` and `black` in my projects. Perhaps it can be configured better. Contributions or suggestions for improvement are welcome :)

## Requirements

- Python 3.12.5+
- poetry (all dependencies manage by poetry)

## Installation
before installation you need generate BOT_TOKEN bot_father

1. Clone the repository:

   ```bash
   git clone git@github.com:clarkreiz/tuting.git
   cd tuting

2. ADD BOT_TOKEN to env
3. ```bash
    export BOT_TOKEN={token_from_bot_father}

4. install dep and run
   ```bash
   poetry install
   poetry run tuting

   
