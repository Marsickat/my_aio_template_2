from sqlalchemy import URL, MetaData
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker


def create_engine(url: URL | str) -> AsyncEngine:
    """
    Создает объект AsyncEngine.

    Args:
        url (URL | str): Строка с URL базы данных.

    Returns:
        Объект AsyncEngine.
    """
    return create_async_engine(url, echo=True, pool_pre_ping=True)


def get_session_maker(engine: AsyncEngine) -> async_sessionmaker:
    """
    Создает объект async_sessionmaker.

    Args:
        engine (AsyncEngine): Объект AsyncEngine.

    Returns:
        Объект async_sessionmaker.
    """
    return async_sessionmaker(engine)


async def proceed_schemas(engine: AsyncEngine, metadata: MetaData):
    """
    Выполняет процедуру создания схемы базы данных.

    Args:
        engine (AsyncEngine): Объект AsyncEngine.
        metadata (MetaData): Объект MetaData.

    Returns:
        None.
    """
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
