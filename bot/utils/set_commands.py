from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    """
    Устанавливает команды бота.

    Args:
        bot (Bot): Объект бота.

    Returns:
         None
    """
    await bot.set_my_commands([
        BotCommand(command="start", description="Выбор подачи котлет"),
        BotCommand(command="echo", description="Отправляет вам ваше же сообщение"),
        BotCommand(command="add_email", description="Добавить e-mail"),
        BotCommand(command="get_emails", description="Посмотреть список e-mail адресов"),
        BotCommand(command="dice", description="Кидает кубик"),
        BotCommand(command="basketball", description="Бросает мяч"),
        BotCommand(command="bowling", description="Бросает шар"),
        BotCommand(command="football", description="Пинает мяч"),
        BotCommand(command="inline_url", description="Ссылки"),
        BotCommand(command="nums_fab", description="Клавиатура с числами"),
        BotCommand(command="form", description="Анкета")
    ])
