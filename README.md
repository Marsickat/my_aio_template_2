Тестовый readme

Зависимости:
1) <b>poetry</b> - Установить poetry - https://python-poetry.org/docs/#installation
2) <b>redis</b> - Установить redis - https://redis.io/docs/getting-started/installation/

Бот запускается командой <b>poetry run python -m bot</b> или <b>make run</b> из папки проекта.


Alembic:

Сгенерировать миграцию:

    make generate NAME=<name>

Отправить миграцию:

    make migrate

Отозвать одну миграцию:

    make downgrade