from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

import bot.keyboards as kb

router = Router()


@router.message(Command("inline_url"))
async def cmd_inline_url(message: Message, bot: Bot):
    """
    Обрабатывает команду /inline_url.

    Parameters:
        message (Message): Объект сообщения.
        bot (Bot): Объект бота.

    Returns:
        None
    """
    builder = kb.inline.inline_url_kb()

    user_id = message.from_user.id
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.button(text="Ваш профиль", url=f"tg://user?id={user_id}")

    await message.answer("Ссылки", reply_markup=builder.as_markup())
