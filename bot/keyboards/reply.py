from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Уроки"), KeyboardButton(text="📊 Прогресс")],
            [KeyboardButton(text="❓ Помощь")]
        ],
        resize_keyboard=True
    )

def lessons_kb(lessons: list):
    buttons = [[KeyboardButton(text=lesson.title)] for lesson in lessons]
    buttons.append([KeyboardButton(text="🔙 Назад")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
