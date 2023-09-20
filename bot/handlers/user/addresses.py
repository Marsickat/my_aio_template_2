from aiogram import Router, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import async_sessionmaker

from database import orm
from bot.states.add_address_state import AddressStates

router = Router()


@router.message(Command("add_email"))
async def cmd_add_email(message: Message, state: FSMContext):
    """
    Обрабатывает команду /add_email.

    Args:
        message (Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.

    Returns:
        None
    """
    await state.set_state(AddressStates.add_address)
    await message.answer("Введите e-mail")


@router.message(AddressStates.add_address)
async def add_email(message: Message, state: FSMContext, sessionmaker: async_sessionmaker):
    """
    Обрабатывает состояние AddressStates.add_address. Также добавляет адрес электронной почты в базу данных.

    Args:
        message (types.Message): Объект сообщения.
        state (FSMContext): Объект FSMContext.
        sessionmaker (async_sessionmaker): asunc_sessionmaker для создания сеанса базы данных.

    Returns:
        None
    """
    entities = message.entities or []
    for item in entities:
        if item.type == "email":
            email = item.extract_from(message.text)
            await orm.add_address(message.from_user.id, html.quote(email), sessionmaker)
            await message.answer(f"Ваша почта записана как - {html.quote(email)}")
            await state.clear()
            break
    else:
        await message.answer("Не обнаружил названия почты в сообщении. Пожалуйста, проверьте данные")


@router.message(Command("get_emails"))
async def cmd_add_email(message: Message, sessionmaker: async_sessionmaker):
    """
    Обрабатывает команду /get_emails.
    Выводит список сохраненных email адресов.

    Args:
        message (Message): Объект сообщения.
        sessionmaker (async_sessionmaker): Объект sessionmaker.

    Returns:
        None
    """

    text = ""
    for address in await orm.get_addresses(message.from_user.id, sessionmaker):
        text += f"{address.email}\n"
    if text:
        await message.answer(text=text)
    else:
        await message.answer(text="Сохраненных email адресов нет")
