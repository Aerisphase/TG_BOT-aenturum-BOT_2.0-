from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.menu_keyboards import categories_keyboard, items_keyboard, item_keyboard, \
    menu_cd
from loader import dp
from utils.db_api.db_commands import get_item


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await list_categories(message)


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()

    if isinstance(message, Message):
        await message.answer("Соберите заказ", reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_items(callback: CallbackQuery, category, **kwargs):
    markup = await items_keyboard(category)

    await callback.message.edit_text(text="Выберите позицию", reply_markup=markup)


async def show_item(callback: CallbackQuery, category, item_id):
    markup = item_keyboard(category, item_id)

    item = await get_item(item_id)
    text = f"Добавить {item.name}?"
    await callback.message.edit_text(text=text, reply_markup=markup)

@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):

    current_level = callback_data.get("level")

    category = callback_data.get("category")

    item_id = int(callback_data.get("item_id"))

    levels = {
        "0": list_categories,  # Отдаем категории
        "1": list_items,  # Отдаем товары
        "2": show_item  # Предлагаем купить товар
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        category=category,
        item_id=item_id
    )
