Тестовый readme

Зависимости:
1) <b>poetry</b> - Установить poetry - https://python-poetry.org/docs/#installation
2) <b>redis</b> - Установить redis - https://redis.io/docs/getting-started/installation/

Бот запускается командой <b>poetry run python -m bot</b> или <b>make run</b> из папки проекта.

Если использовать docker:
При первом запуске использовать команду:

    docker-compose run bot bash -c "poetry run alembic revision -m=init --autogenerate && poetry run alembic upgrade head"

В случае изменений в структуре бота запускать командой:

    docker-compose up --build



Alembic:

Сгенерировать миграцию:

    make generate NAME=<name>

Отправить миграцию:

    make migrate

Отозвать одну миграцию:

    make downgrade