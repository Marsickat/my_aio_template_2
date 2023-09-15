from aiogram.fsm.state import StatesGroup, State


class FormStates(StatesGroup):
    name = State()
    like_programming = State()
    language = State()
