from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(Command('signup'))
async def signup_handler(message: Message):
    await message.answer(text='еблан')