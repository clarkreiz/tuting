import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .handlers import add_student, start

TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(add_student.router)

    await dp.start_polling(bot)

def run_main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('bot.log')
        ]
    )
    asyncio.run(main())

if __name__ == "__main__":
    run_main()
