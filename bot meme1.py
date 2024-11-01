import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router


async def main():
    bot = Bot(token='7507413811:AAEVWakpJU4VQmQBDQh-ZjNe7HJEG-LwgWo')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is shutting down...')




