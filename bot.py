import asyncio
import logging

import uvloop

from bot import start_bot
from config import bot_token

logger = logging.getLogger("aiogram")

if __name__ == "__main__":
    try:
        uvloop.install()
        asyncio.run(start_bot(bot_token))
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Bot stopped!")
