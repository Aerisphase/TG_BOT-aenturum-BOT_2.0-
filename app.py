from aiogram import executor
from utils.db_api.database import create_db

from handlers.users.menu import show_menu
from loader import dp
from utils.notify_admins import on_startup_notify
from handlers.users.start import bot_start
from handlers.users.help import bot_help
from handlers.users.admins import show_admins


async def on_startup(dispatcher):
    # Уведомляет о запуске
    await on_startup_notify(dispatcher)
    await create_db()


async def start(dispatcher):
    # Выполняет команду /start
    await bot_start(dispatcher)


async def helping(dispatcher):
    # Выполняет команду /help
    await bot_help(dispatcher)


async def admins(dispatcher):
    # Выполняет команду /admins
    await show_admins(dispatcher)


async def menu(dispatcher):
    # Выполняет команду /menu
    await show_menu(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
