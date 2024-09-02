# Tutor Accounting Bot

A bookkeeping project designed for tutors and private educators. The frontend is built using Python, leveraging Telegram for user interaction and the `aiogram` library. The backend will be developed separately in a different repository using Go (Golang) and PostgreSQL.

## Overview

This repository contains the code for the Telegram bot. The bot uses an `aiohttp` client to send and receive messages from the backend.

## Features

- **User-friendly Telegram interface**: Interact with the bot via Telegram.
- **State management with FSM**: Efficiently handle user states and dialogues.
- **Async communication**: Uses `aiohttp` for non-blocking requests to the backend.

## Requirements

- Python 3.11+
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

   
