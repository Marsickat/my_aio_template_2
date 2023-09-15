from aiogram import Router
from aiogram.enums import DiceEmoji
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("dice"))
async def cmd_dice(message: Message):
    """
    Обрабатывает команду /dice.
    Отправляет кубик, который выдает случайное число.

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(Command("basketball"))
async def cmd_basketball(message: Message):
    """
    Обрабатывает команду /basketball.
    Отправляет баскетбольный мяч, пытающийся попасть в корзину.

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)


@router.message(Command("bowling"))
async def cmd_basketball(message: Message):
    """
    Обрабатывает команду /bowling.
    Отправляет шар для боулинга, пытающийся сбить кегли.

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    await message.answer_dice(emoji=DiceEmoji.BOWLING)


@router.message(Command("football"))
async def cmd_basketball(message: Message):
    """
    Обрабатывает команду /football.
    Отправляет футбольный мяч, пытающийся попасть в ворота.

    Args:
        message (Message): Объект сообщения.

    Returns:
        None
    """
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)
