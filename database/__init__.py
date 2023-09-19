from os import getenv

from sqlalchemy import URL

from .engine import create_engine, get_session_maker, proceed_schemas
from .redis import redis
from . import models, orm

postgres_url = URL.create(
    drivername=getenv(key="POSTGRES_DRIVERNAME"),
    username=getenv(key="POSTGRES_USER"),
    password=getenv(key="POSTGRES_PASSWORD"),
    host=getenv(key="POSTGRES_HOST"),
    port=getenv(key="POSTGRES_PORT"),
    database=getenv(key="POSTGRES_DB")
)
async_engine = create_engine(postgres_url)
async_sessionmaker = get_session_maker(async_engine)
