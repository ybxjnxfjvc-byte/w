from aiogram.fsm.state import State, StatesGroup

class LearningStates(StatesGroup):
    selecting_lesson = State()    # выбор урока
    answering_question = State()  # ответ на вопрос
    waiting_for_feedback = State()# обратная связь
