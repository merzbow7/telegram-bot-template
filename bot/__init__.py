import logging

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.handlers import register_handlers


async def startup(dp: Dispatcher) -> None:
    ...


async def shutdown(dp: Dispatcher) -> None:
    ...


async def setup_bot_commands(bot: Bot):
    bot_commands = [
        types.BotCommand(command="/cancel", description="cancel"),
    ]
    await bot.set_my_commands(bot_commands)


async def start_bot(token: str) -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
    await setup_bot_commands(bot)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    register_handlers(dp)

    try:
        await startup(dp)
        await dp.start_polling()
    except Exception as err:
        logging.error(err)
    finally:
        await shutdown(dp)
        await bot.session.close()
