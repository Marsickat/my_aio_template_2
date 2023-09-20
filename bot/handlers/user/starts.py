from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import async_sessionmaker

import bot.keyboards as kb
from database import orm

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, sessionmaker: async_sessionmaker):
    """
    Обрабатывает команду /start.
    Добавляет пользователя в базу данных, если он там отсутствует.

    Args:
        message (Message): Объект сообщения.
        sessionmaker (async_sessionmaker): Объект sessionmaker.

    Returns:
        None
    """
    user = await orm.get_user(message.from_user.id, sessionmaker)
    if not user:
        await orm.add_user(message.from_user.id,
                           message.from_user.username,
                           message.from_user.first_name,
                           message.from_user.last_name,
                           sessionmaker)
        await message.answer("Проведена регистрация")
    await message.answer("Здравствуйте, вот вам кнопки", reply_markup=kb.reply.yes_no())


@router.message(F.text.casefold() == "да")
async def answer_with_puree(message: Message):
    """
    Обрабатывает текстовое сообщение "да".

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    await message.reply(f"Вы нажали {message.text}", reply_markup=ReplyKeyboardRemove())


@router.message(F.text.casefold() == "нет")
async def answer_without_puree(message: Message):
    """
    Обрабатывает текстовое сообщение "нет".

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    await message.reply(f"Вы нажали {message.text}", reply_markup=ReplyKeyboardRemove())
