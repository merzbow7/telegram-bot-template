from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from resource.callbacks import cb_apples_count


def buy_keyboard(text: str = '') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton(text=text if text else str(key),
                                    callback_data=cb_apples_count.new(count=key))
               for key in range(1, 7)]
    keyboard.add(*buttons)
    return keyboard


def sport_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"ЦСКА", url="https://www.sports.ru/cska/"),
         InlineKeyboardButton(text=f"Washington Capitals", url="https://www.sports.ru/washington-capitals/"), ],
        [InlineKeyboardButton(text=f"San Antonio Spurs", url="https://www.sports.ru/san-antonio-spurs/"),
         InlineKeyboardButton(text=f"Phoenix Sans", url="https://www.sports.ru/phoenix-suns/"), ],
    ])
    return keyboard
