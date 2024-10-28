import asyncio
from aiogram import Bot, Dispatcher
from app.hendlers import router


async def main():
    bot = Bot(token='7923155027:AAG8zvHmsuFDT0y1xakOtYtPPDCLok3ypJE')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is shutting down...')



