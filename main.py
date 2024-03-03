from settings import bot_credentials
from aiogram import Dispatcher
from aiogram import Bot
import logging
import asyncio

from routers import router as main_router


async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    bot = Bot(token=bot_credentials.BOT_TOKEN)
    dp.include_routers(main_router)
    await dp.start_polling(bot)

asyncio.run(main())