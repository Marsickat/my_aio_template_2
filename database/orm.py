from typing import Optional

from sqlalchemy.ext.asyncio import async_sessionmaker

from database import redis
from database.models import UserModel, AddressModel


async def add_address(user_id: int, email: str, sessionmaker: async_sessionmaker):
    """
    Добавляет адрес электронной почты в базу данных.

    Args:
        user_id (int): ID пользователя Telegram.
        email (str): Адрес электронной почты.
        sessionmaker (async_sessionmaker): Async_sessionmaker для создания сеанса базы данных.

    Returns:
         None
    """
    async with sessionmaker() as session:
        session.add(AddressModel(user_id=user_id,
                                 email=email))
        await session.commit()


async def add_user(user_id: int, username: Optional[str], first_name: Optional[str], last_name: Optional[str],
                   sessionmaker: async_sessionmaker):
    """
    Добавляет пользователя в базу данных.

    Args:
        user_id (int): ID пользователя Telegram.
        username (Optional[str]): Username пользователя Telegram.
        first_name (Optional[str]): Имя пользователя Telegram.
        last_name (Optional[str]): Фамилия пользователя Telegram.
        sessionmaker (async_sessionmaker): Async_sessionmaker для создания сеанса базы данных.

    Returns:
         None
    """
    async with sessionmaker() as session:
        user = UserModel(user_id=user_id,
                         username=username,
                         first_name=first_name,
                         last_name=last_name)
        session.add(user)
        await redis.set(name="tg_id_" + str(user_id), value=1)
        await session.commit()


async def get_user(user_id: int, sessionmaker: async_sessionmaker):
    """
    Получает пользователя из базы данных.

    Args:
        user_id (int): ID пользователя Telegram.
        sessionmaker (async_sessionmaker): Async_sessionmaker для создания сеанса базы данных.

    Returns:
         None
    """
    # async with sessionmaker() as session:
    #     # user = (await session.execute(select(UserModel).where(UserModel.user_id == user_id))).one_or_none()
    #     user = await session.get(UserModel, user_id)
    #     return user
    return await redis.get(name="tg_id_" + str(user_id))
