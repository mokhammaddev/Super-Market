import asyncio
import logging
from aiogram import F
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from app.settings import settings
from app.functions import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token, parse_mode='html')
dp = Dispatcher()
dp.message.register(get_start, F.text == '/start')
dp.message.register(set_commands, Command(commands='inline'))
dp.callback_query.register(get_menu, F.data.startswith('uzb'))
dp.callback_query.register(get_again_start, F.data.startswith('edit_language'))
dp.callback_query.register(get_english_start, F.data.startswith('eng'))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
