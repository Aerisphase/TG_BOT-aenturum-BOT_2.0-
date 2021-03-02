from environs import Env
import os

env = Env()
env.read_env()

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}"

USERNAME_ADMIN1 = os.getenv("USERNAME_ADMIN1")
USERNAME_ADMIN2 = os.getenv("USERNAME_ADMIN2")
