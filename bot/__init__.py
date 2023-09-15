from os import getenv

from dotenv import load_dotenv

load_dotenv("../.env")
test = getenv("BOT_TOKEN")
