from aiogram import Router, types, F
from bot.keyboards.reply import main_menu_kb

router = Router()

@router.message(F.text == "📚 Уроки")
async def show_lessons(message: types.Message):
    # здесь логика получения списка уроков из БД
    await message.answer("Выберите урок:", reply_markup=lessons_kb(lessons))

@router.message(F.text == "📊 Прогресс")
async def show_progress(message: types.Message):
    # статистика пользователя
    await message.answer("Ваш прогресс: ...", reply_markup=main_menu_kb())

@router.message(F.text == "❓ Помощь")
async def show_help(message: types.Message):
    await message.answer(
        "📖 Справка:\n"
        "/start — главное меню\n"
        "Выбирайте уроки и отвечайте на вопросы!",
        reply_markup=main_menu_kb()
    )
