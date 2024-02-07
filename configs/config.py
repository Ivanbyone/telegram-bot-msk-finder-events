import os
from pathlib import Path
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv("token")
ADMIN_ID = os.getenv("admin_id")

DB_URL = os.getenv("url_db")
DB_NAME = os.getenv("db_name")

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher()
