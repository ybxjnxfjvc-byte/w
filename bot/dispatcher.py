from aiogram import Dispatcher
from bot.handlers import start, menu, lessons

def setup_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(lessons.router)
    return dp
