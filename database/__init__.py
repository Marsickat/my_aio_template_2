from os import getenv

from sqlalchemy import URL

from . import models, orm
from .engine import create_engine, get_session_maker, proceed_schemas

postgres_url = URL.create(
    drivername=getenv(key="DB_DRIVERNAME"),
    username=getenv(key="DB_USERNAME"),
    password=getenv(key="DB_PASSWORD"),
    host=getenv(key="DB_HOST"),
    port=getenv(key="DB_PORT"),
    database=getenv(key="DB_DATABASE")
)
async_engine = create_engine(postgres_url)
async_sessionmaker = get_session_maker(async_engine)
