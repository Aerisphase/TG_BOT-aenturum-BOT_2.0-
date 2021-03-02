from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n"
                         f"Вас приветсвует Телеграм Бот AenturumBeta.\n"
                         f"Данный бот находится в стадии разработки\n"
                         f"Если у вас появились вопросы - воспользуйтесь командой /help")
