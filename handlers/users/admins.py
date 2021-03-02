
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.choice_buttons import choice
from loader import dp


@dp.message_handler(Command("admins"))
async def show_admins(message: Message):
    await message.answer(text="По вопросам технической поддержки пишите Яну \n"
                              "По вопросам баз данных пишите Адриану",
                         reply_markup=choice)
