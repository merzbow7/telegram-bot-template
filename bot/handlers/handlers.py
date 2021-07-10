from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from resource.callbacks import cb_apples_count
from resource.keyboards import buy_keyboard, sport_keyboard


async def sport(message: types.Message) -> None:
    await message.answer("Which your favorite team??", reply_markup=sport_keyboard())


async def echo(message: types.Message) -> None:
    await message.answer("How many apples do you want buy?", reply_markup=buy_keyboard())


async def buy_apples(call: types.CallbackQuery, callback_data: dict) -> None:
    await call.answer(f'You want {callback_data["count"]} {callback_data["@"]}')


def register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(sport, Command("sport"))
    dp.register_message_handler(echo, content_types=['text'])
    dp.register_callback_query_handler(buy_apples, cb_apples_count.filter())
