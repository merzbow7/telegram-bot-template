import os

from dotenv import load_dotenv

load_dotenv()
bot_token: str = os.environ.get('BOT_TOKEN')
