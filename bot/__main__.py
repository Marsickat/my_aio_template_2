import bot  # initial import

import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv

import database as db
import middlewares as mw
import handlers
import utils

load_dotenv("../.env")


async def main():
    # Инициализация
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    bot_obj = Bot(token=getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)

    # Выбор хранилища
    dp = Dispatcher(storage=MemoryStorage())
    # dp = Dispatcher(storage=RedisStorage.from_url(getenv("REDIS_URL")))

    # Инициализация базы данных
    await db.proceed_schemas(db.async_engine, db.models.BaseModel.metadata)

    # Подключение хэндлеров
    dp.include_routers(handlers.user_router, handlers.admin_router)

    # Подключение мидлварей
    # dp.message.middleware(mw.DatabaseMiddleware())

    # Установка команд в меню
    await utils.set_commands(bot_obj)

    # Подключение функций запуска и остановки
    dp.startup.register(utils.send_message_startup)
    dp.shutdown.register(utils.send_message_shutdown)

    # Запуск
    await bot_obj.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot_obj, sessionmaker=db.async_sessionmaker)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
