from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import types
from datetime import datetime
import requests
import app.keyboards as keyboards
import json
from dotenv import load_dotenv
import os
from aiogram.types import Message, URLInputFile

router = Router()


#url изъят в env
load_dotenv()
URL = (os.getenv('URL'))


#Выводит с помощью команды при старте
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Доброе время суток,  {message.chat.username},  давай пошутим?", reply_markup=keyboards.main)


#Выводит с помощью команды "/"
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи\n'
                         'Доступные команды:\n'
                         '*/date- Показывает  текущую дату\n'
                         '*/time- Показывает текущее время\n'
                         '*/meme- Выводит рандомную шутку\n'
                         '*/photomem- Выводит рандомную картинку с мемом\n'
                         '*/datetime - Выводит текущие дату и время')


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'заказчик')
async def balance(message: Message):
    await message.answer('хуесос!')


#Выводит с помощью команды "/"
@router.message(Command('date'))
async def cmd_date(message: Message):
    await message.answer(f"Сегодняшняя дата: {datetime.now():%d.%m.%Yг.}")


#Выводит с помощью команды "/"
@router.message(Command('datetime'))
async def cmd_datetime(message: Message):
    await message.answer(f"Сегодняшние дата: {datetime.now():%d.%m.%Yг.; текущее время: %H:%M:%S}")


#Выводит с помощью команды "/"
@router.message(Command('time'))
async def cmd_time(message: Message):
    await message.answer(f"Время: {datetime.now():%H:%M:%S}")


#Выводит с помощью команды "/"
@router.message(Command('meme'))
async def cmd_meme(message: Message):
    await message.answer(f" {catch_joke_error()}")


#Выводит с помощью команды "/"
@router.message(Command('photomem'))
async def cmd_photo(message: Message):
    await message.answer_photo(URLInputFile(f" {getMeme()}"))


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'Помощь')
async def cmd_help_key(message: Message):
    await message.answer('Вы нажали на кнопку помощи\n'
                         'Доступные команды:\n'
                         '*/date- Показывает  текущую дату\n'
                         '*/time- Показывает текущее время\n'
                         '*/meme- Выводит рандомную шутку\n'
                         '*/photomem- Выводит рандомную картинку с мемом\n'
                         '*/datetime - Выводит текущие дату и время')


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'Дата')
async def cmd_date_key(message: Message):
    await message.answer(f"Сегодняшняя дата: {datetime.now():%d.%m.%Yг.}")


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'Время')
async def cmd_time_key(message: Message):
    await message.answer(f"Время: {datetime.now():%H:%M:%S}")


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'Анекдоты')
async def cmd_meme_key(message: Message):
    await message.answer(f" {catch_joke_error()}")


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'хаха')
async def cmd_meme_key(message: Message):
    await message.answer(f" {catch_joke_error()}")


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'Картинки')
async def cmd_meme_key(message: Message):
    print(f"Инициирован запрос НА МЕМАСИК в: {datetime.now()}")
    await message.answer_photo(URLInputFile(f" {getMeme()}"))
    print(f"Картинка отправлена в: {datetime.now()}")


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'лол')
async def cmd_meme_key(message: Message):
    await message.answer(f" {catch_joke_error()}")


#Выводит с помощью ReplyKeyboardMarkup
@router.message(F.text == 'Дата и время')
async def cmd_datetime_key(message: Message):
    await message.answer(f"Сегодняшние дата: {datetime.now():%d.%m.%Yг.; текущее время: %H:%M:%S}")


#Дает конкретный ответ на неизвестные ему сообщения
@router.message()
async def balance(message: types.Message):
    await message.answer("Я вас не понимаю, обратитесь к команде /help, за помощью")


#url изъят в env
load_dotenv()
IMAGE_URL = (os.getenv('IMAGE_URL'))


#ЗДЕСЬ НЕТ РЕКУРСИИ
def getMeme():
    try:
        memeApiResponse = requests.get(os.getenv('IMAGE_URL'))
        memeJson = json.loads(memeApiResponse.text)
        return memeJson['url']
    except Exception:
        getMeme()


#Использовалась рекурсия для мемов*
def catch_joke_error():
    try:
        response = requests.get(URL)
        json_joke = json.loads(response.text, strict=False)
        return json_joke['content']
    except Exception:
        return catch_joke_error()



