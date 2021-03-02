from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import POSTGRES_URI

db = Gino()



async def create_db():
    # Устанавливаем связь с базой данных
    await db.set_bind(POSTGRES_URI)
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()

    # Создаем таблицы
    # await db.gino.drop_all()
    # await db.gino.create_all()