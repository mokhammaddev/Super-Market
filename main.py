import asyncio
import asyncpg
import logging
from aiogram import F
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from app.settings import settings
from app.functions import *
from db.dbmiddleware import DbSession

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token, parse_mode='html')
# pool_connect = await create_pool()
# db.updatde.middileware.register(DbSession(pool_connect))
dp = Dispatcher()
dp.message.register(get_start, F.text == '/start')
dp.message.register(set_commands, Command(commands='inline'))
dp.callback_query.register(get_menu, F.data.startswith('uzb'))
dp.callback_query.register(get_again_start, F.data.startswith('edit_language'))
dp.callback_query.register(get_vacancies, F.data.startswith('vacancy'))
dp.callback_query.register(get_start, F.data.startswith('back_vacancy'))
dp.callback_query.register(get_menu, F.data.startswith('menu'))
# dp.callback_query.register(get_kassir, F.data.startswith("kassir"))
dp.message.register(get_kassir, F.text == 'Kassir 💰')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
