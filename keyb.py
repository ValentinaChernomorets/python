from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺 RU"),
            KeyboardButton(text="🇲🇩 MD"),
            KeyboardButton(text="🇬🇧 EN"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True)