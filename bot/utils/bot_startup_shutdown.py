from os import getenv

from aiogram import Bot


async def send_message_startup(bot: Bot):
    """
    Отправляет администраторам сообщение о запуске бота.

    Args:
        bot (Bot): Объект бота.

    Returns:
         None
    """
    text = "Бот запущен!\n\n"
    for user in eval(getenv("ADMINS")):
        await bot.send_message(user, text)


async def send_message_shutdown(bot: Bot):
    """
    Отправляет администраторам сообщение об остановке бота.

    Args:
        bot (Bot): Объект бота.

    Returns:
         None
    """
    text = "Бот остановлен\n\n"
    for user in eval(getenv("ADMINS")):
        await bot.send_message(user, text)
