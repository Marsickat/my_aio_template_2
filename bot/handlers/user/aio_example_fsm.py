import emoji
from aiogram import Router, html, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from emoji import emojize

import bot.keyboards as kb
from bot.states import FormStates

router = Router()


@router.message(Command("form"))
async def cmd_form(message: Message, state: FSMContext):
    """
    Обрабатывает команду /form.

    Args:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    await state.set_state(FormStates.name)
    await message.answer("Привет! Как тебя зовут?", reply_markup=ReplyKeyboardRemove())


@router.message(F.text.casefold() == "cancel")
async def cancel_state(message: Message, state: FSMContext):
    """
    Отменяет текущее состояние диалога, если получает текстовое сообщение "cancel".

    Args:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Отменено", reply_markup=ReplyKeyboardRemove())


@router.message(FormStates.name)
async def process_name(message: Message, state: FSMContext):
    """
    Обрабатывает ввод имени пользователя в состояние FormStates и обновляет состояние FormStates в like_programming.

    Args:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    await state.update_data(name=message.text)
    await state.set_state(FormStates.like_programming)
    await message.answer(f"Приятно познакомится, {html.quote(message.text)}!\nТебе нравится программирование?",
                         reply_markup=kb.reply.yes_no())


@router.message(FormStates.like_programming, F.text.casefold() == "да")
async def process_like_programming(message: Message, state: FSMContext):
    """
    Обрабатывает состояние FormStates.like_programming при согласии пользователя.

    Args:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    await state.set_state(FormStates.language)
    await message.reply("Круто! Я тоже!\nКакой язык программирования ты используешь?",
                        reply_markup=ReplyKeyboardRemove())


@router.message(FormStates.like_programming, F.text.casefold() == "нет")
async def process_dont_like_programming(message: Message, state: FSMContext):
    """
    Обрабатывает состояние FormStates.like_programming при несогласии пользователя.

    Args:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    data = await state.get_data()
    await state.clear()
    await message.answer("Ничего страшного.\nУвидимся!",
                         reply_markup=ReplyKeyboardRemove())
    name = data["name"]
    await message.answer(f"Я буду иметь ввиду, что ты, {html.quote(name)}, не любишь программировать, жаль...")


@router.message(FormStates.like_programming)
async def process_unknown_like_programming(message: Message):
    """
    Обрабатывает состояние FormStates.like_programming при несоответствующем ответе пользователя.

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    await message.reply(f"Я не понимаю тебя {emoji.emojize(':pensive_face:')}")


@router.message(FormStates.language)
async def process_language(message: Message, state: FSMContext):
    """
    Обрабатывает состояние FormStates.language.

    Args:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    data = await state.get_data()
    await state.clear()

    if message.text.casefold() == "python":
        await message.reply(f"Python, говоришь? Я тоже! {emojize(':grinning_face:')}")

    name = data["name"]
    await message.answer(
        f"Я буду иметь ввиду, что ты, {html.quote(name)}, любишь программировать на {html.quote(message.text)}.",
        reply_markup=ReplyKeyboardRemove()
    )
