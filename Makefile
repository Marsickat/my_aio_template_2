run: migrate
	poetry run python -m bot

generate:
	alembic revision -m="$(NAME)" --autogenerate

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1
