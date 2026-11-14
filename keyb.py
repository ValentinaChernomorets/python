from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translations import texts

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
# Step 5
# Create menu
# keyb_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="contacts"),
#             KeyboardButton(text="information"),
#             KeyboardButton(text="services"),
#             KeyboardButton(text="schedule lessons"),
#             KeyboardButton(text="news"),
#         ],
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=True)
# Step 6
# Create menu depending on language
def create_menu(language):
    keyb_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=texts[language]["menu"]["contacts"]),
                KeyboardButton(text=texts[language]["menu"]["information"])
            ],
            [
                KeyboardButton(text=texts[language]["menu"]["services"]),
                KeyboardButton(text=texts[language]["menu"]["schedule"])
            ],
            [
                KeyboardButton(text=texts[language]["menu"]["news"])
            ]
        ],
        resize_keyboard=True
    )

    return keyb_menu

question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Хочу добавиться в канал",
                callback_data="add_channel"
            )
        ],
        [
            InlineKeyboardButton(
                text="Не хочу добавляться в канал",
                callback_data="no_channel"
            )
        ]
    ]
)