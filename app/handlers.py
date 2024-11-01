from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import types
from datetime import datetime
import requests
import app.keyboards as keyboards
import json

router = Router()


URL = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Добрый день,  {message.chat.username},  давай пошутим?", reply_markup=keyboards.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи\n'
                         'Доступные команды:\n'
                         '*/date- Показывает  текущую дату\n'
                         '*/time- Показывает текущее время\n'
                         '*/meme- Выводит рандомную шутку\n'
                         '*/datetime - Выводит текущие дату и время')


@router.message(F.text == 'Помощь')
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи\n'
                         'Доступные команды:\n'
                         '*/date- Показывает  текущую дату\n'
                         '*/time- Показывает текущее время\n'
                         '*/meme- Выводит рандомную шутку\n'
                         '*/datetime - Выводит текущие дату и время')


@router.message(F.text == 'заказчик')
async def balance(message: Message):
    await message.answer('хуесос!')


@router.message(Command('date'))
async def cmd_time(message: Message):
    await message.answer(f"Сегодняшняя дата: {datetime.now().date()} ")


@router.message(Command('datetime'))
async def cmd_time(message: Message):
    await message.answer(f"Сегодняшние дата и время: {datetime.now()} ")


@router.message(Command('time'))
async def cmd_time(message: Message):
    await message.answer(f"Время: {datetime.now().time()} ")


@router.message(Command('meme'))
async def cmd_time(message: Message):
    r = requests.get(URL)
    await message.answer(f" {r.text} ")


@router.message(F.text == 'Дата')
async def balance(message: Message):
    await message.answer(f"Сегодняшняя дата: {datetime.now().date()} ")


@router.message(F.text == 'Время')
async def cmd_time(message: Message):
    await message.answer(f"Время: {datetime.now().time()} ")


@router.message(F.text == 'Анекдоты')
async def cmd_time(message: Message):
    await message.answer(f" {catch_joke_error()} ")


@router.message(F.text == 'Дата и время')
async def cmd_time(message: Message):
    await message.answer(f"Сегодняшние дата и время: {datetime.now()} ")


#Использовалась рекурсия*
def catch_joke_error():
    try:
        response = requests.get(URL)
        print(response.text)
        json_joke = json.loads(response.text, strict=False)
        return json_joke['content']
    except Exception:
        return catch_joke_error()



