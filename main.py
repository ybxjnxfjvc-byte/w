import asyncio
import logging
from aiogram import Bot
from bot.config import Config
from bot.dispatcher import setup_dispatcher
from bot.database.crud import init_db

async def main():
    logging.basicConfig(level=logging.INFO)
    await init_db()
    bot = Bot(token=Config.BOT_TOKEN)
    dp = setup_dispatcher()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
