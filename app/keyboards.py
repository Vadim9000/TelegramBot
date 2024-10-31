from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Дата')],
                                     [KeyboardButton(text='Время')],
                                     [KeyboardButton(text='Помощь'),
                                      KeyboardButton(text='Анекдоты')]])
