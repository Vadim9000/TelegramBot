from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Команды')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О нас')]])
