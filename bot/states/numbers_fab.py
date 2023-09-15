from aiogram.fsm.state import StatesGroup, State


class NumbersFabStates(StatesGroup):
    change = State()
    finish = State()
