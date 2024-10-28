from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')


@router.message(F.text == 'Влад')
async def balance(message: Message):
    await message.answer('лох!')
