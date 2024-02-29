from settings import BOT_TOKEN
from aiogram import Dispatcher
from aiogram import Bot
import logging
import asyncio

from routers import router as main_router



async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    bot = Bot(token=BOT_TOKEN)
    dp.include_routers(main_router)
    await dp.start_polling(bot)

asyncio.run(main())