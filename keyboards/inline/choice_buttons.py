from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import USERNAME_ADMIN1, USERNAME_ADMIN2

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Адриан", url=USERNAME_ADMIN1),
            InlineKeyboardButton(text="Ян", url=USERNAME_ADMIN2),
        ]
])
