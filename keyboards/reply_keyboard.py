from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from settings.config import KEYBOARD

MAIN_MENU = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=KEYBOARD['BASE_QUESTIONS'])
        ],
        [
            KeyboardButton(text=KEYBOARD['MY_PROBLEM'])
        ]
    ],
    resize_keyboard=True
)
