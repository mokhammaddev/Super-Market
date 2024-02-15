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
dp = Dispatcher()
dp.message.register(get_start, F.text == '/start')
dp.message.register(set_commands, Command(commands='inline'))
dp.callback_query.register(get_menu, F.data.startswith('uzb'))
dp.callback_query.register(get_again_start, F.data.startswith('edit_language'))
dp.callback_query.register(get_vacancies, F.data.startswith('vacancy'))
dp.callback_query.register(get_menu, F.data.startswith('menu'))
dp.callback_query.register(get_settings, F.data.startswith('settings_uzb'))
dp.callback_query.register(get_about, F.data.startswith('about_uzb'))
# dp.callback_query.register(get_cashier, F.data.startswith('cashier'))
# dp.message.register(get_start_cashier)
# dp.message.register(anonym_text_delete)


##############################################################################


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
