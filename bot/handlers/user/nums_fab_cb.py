from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import bot.callbacks as cb
import bot.keyboards as kb
from bot.states import NumbersFabStates

router = Router()


@router.message(Command("nums_fab"))
async def cmd_nums_fab(message: Message, state: FSMContext):
    """
    Обрабатывает команду /nums_fab.

    Parameters:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    await state.set_state(NumbersFabStates.change)
    await state.update_data(value=0)
    await message.answer("Выберите действие с числом: 0", reply_markup=kb.inline.numbers_fab_kb())


@router.callback_query(cb.NumbersCallbackFactory.filter())
async def callback_nums_change_fab(callback: CallbackQuery, callback_data: cb.NumbersCallbackFactory,
                                   state: FSMContext):
    """
    Callback-функция, обрабатывающая изменение чисел.

    Args:
        callback (CallbackQuery): Объект CallbackQuery.
        callback_data (cb.NumbersCallbackFactory): Объект callback-данных.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    data = await state.get_data()
    new_value = data["value"] + callback_data.value
    await state.update_data(value=new_value)
    if callback_data.action == "change":
        data["value"] += callback_data.value
        await cb.update_nums_fab(callback.message, data["value"])
    else:
        await callback.message.edit_text(f"Итого: {data['value']}")
    await callback.answer()
