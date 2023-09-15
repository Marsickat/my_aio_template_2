from aiogram.types import Message

import bot.keyboards as kb


async def update_nums_fab(message: Message, new_value: int):
    """
    Обновляет сообщение новыми значениями.

    Args:
        message (Message): Объект сообщения.
        new_value (int): Новое числовое значение.

    Returns:
        None
    """
    await message.edit_text(f"Выберите действие с числом: {new_value}", reply_markup=kb.inline.numbers_fab_kb())
