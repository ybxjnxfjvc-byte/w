from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.states.learning import LearningStates
from bot.database.crud import get_lesson, save_answer

router = Router()

@router.message(F.text.startswith("Урок"))
async def start_lesson(message: types.Message, state: FSMContext):
    lesson_id = int(message.text.split()[1])  # упрощённо
    await state.update_data(lesson_id=lesson_id, question_index=0)
    await send_question(message, state)

async def send_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # получаем вопрос из БД по lesson_id и question_index
    question = "..."
    await message.answer(question, reply_markup=answer_kb())
    await state.set_state(LearningStates.answering_question)

@router.message(LearningStates.answering_question)
async def handle_answer(message: types.Message, state: FSMContext):
    # проверка ответа, запись в БД
    await state.clear()
    await message.answer("✅ Ответ принят!", reply_markup=main_menu_kb())
