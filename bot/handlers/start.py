from aiogram import Router, types
from aiogram.filters import Command
from bot.database.crud import get_or_create_user
from bot.keyboards.reply import main_menu_kb

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    user = await get_or_create_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username
    )
    await message.answer(
        f"🎓 Добро пожаловать в обучающий бот, {user.full_name}!\n"
        "Я помогу вам освоить новый материал. Выберите действие:",
        reply_markup=main_menu_kb()
    )
