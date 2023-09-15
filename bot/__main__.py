import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

import bot.handlers
import bot.utils
import database as db


async def main():
    # Инициализация
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    bot_obj = Bot(token=getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)

    # Выбор хранилища
    dp = Dispatcher(storage=MemoryStorage())
    # dp = Dispatcher(storage=RedisStorage(bot.utils.redis))

    # Инициализация базы данных (вместо alembic)
    # await db.proceed_schemas(db.async_engine, db.models.BaseModel.metadata)

    # Подключение хэндлеров
    dp.include_routers(bot.handlers.user_router, bot.handlers.admin_router)

    # Подключение мидлварей
    # dp.message.middleware(mw.DatabaseMiddleware())

    # Установка команд в меню
    await bot.utils.set_commands(bot_obj)

    # Подключение функций запуска и остановки
    dp.startup.register(bot.utils.send_message_startup)
    dp.shutdown.register(bot.utils.send_message_shutdown)

    # Запуск
    await bot_obj.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot_obj, sessionmaker=db.async_sessionmaker)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
