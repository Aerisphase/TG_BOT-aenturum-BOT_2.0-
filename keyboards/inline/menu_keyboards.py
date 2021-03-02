from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.db_commands import get_categories, get_items

menu_cd = CallbackData("show_menu", "level", "category", "item_id")
buy_item = CallbackData("buy", "item_id")


def make_callback_data(level, category="0", item_id="0"):

    return menu_cd.new(
        level=level,
        category=category,
        item_id=item_id
    )


async def categories_keyboard():

    CURRENT_LEVEL = 0

    markup = InlineKeyboardMarkup(row_width=3)

    # Забираем список товаров из базы данных с РАЗНЫМИ категориями и проходим по нему
    categories = get_categories()
    for category in await categories:
        # Сформируем текст, который будет на кнопке
        button_text = f"{category.category_name}"

        # Сформируем колбек дату, которая будет на кнопке. Следующий уровень - текущий + 1, и перечисляем категории
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category.category_code)

        # Вставляем кнопку в клавиатуру
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Возвращаем созданную клавиатуру в хендлер
    return markup


async def items_keyboard(category):
    CURRENT_LEVEL = 1

    markup = InlineKeyboardMarkup(row_width=1)

    items = await get_items(category)
    for item in items:

        button_text = f"{item.name}"

        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           item_id=item.id,
                                           )
        markup.insert(
            InlineKeyboardButton(
                text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="← Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             category=category,))

    )
    return markup


def item_keyboard(category, item_id):

    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text=f"Добавить",
            callback_data=buy_item.new(item_id=item_id)
        )
    )
    markup.row(
        InlineKeyboardButton(
            text="← Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             category=category))
    )
    return markup
