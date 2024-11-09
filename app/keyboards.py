from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Дата')],
                                     [KeyboardButton(text='Время')],
                                     [KeyboardButton(text='Помощь')],
                                     [KeyboardButton(text='Дата и время')],
                                     [KeyboardButton(text='Картинки'),
                                      KeyboardButton(text='Анекдоты')]])
