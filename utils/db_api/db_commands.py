from typing import List

from sqlalchemy import and_

from utils.db_api.models import Item
from utils.db_api.database import db


async def add_item(**kwargs):
    new_item = await Item(**kwargs).create()
    return new_item


async def get_categories() -> List[Item]:
    return await Item.query.distinct(Item.category_name).gino.all()


# async def count_items(category_code):
#
#     conditions = [Item.category_code == category_code]
#
#     total = await db.select([db.func.count()]).where(
#         and_(*conditions)
#     ).gino.scalar()
#     return total


async def get_items(category_code) -> List[Item]:
    item = await Item.query.where(
        and_(Item.category_code == category_code)
    ).gino.all()
    return item


async def get_item(item_id) -> Item:
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item
