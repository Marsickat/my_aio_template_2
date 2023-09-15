from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("echo"))
async def cmd_echo(message: Message):
    """
    Отправляет пользователю текст его же сообщения.

    Parameters:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    print(message.text)
    await message.answer(message.text)
