import asyncio
import logging

from aiogram import F
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from app.settings import settings


from aiogram.types import Message, CallbackQuery
from app.inline import start_inline_keyboard, menu_uzb_inline_keyboard
from app.commands import set_commands


async def get_start(message: Message, bot: Bot):
    await set_commands(bot)
    await message.answer(f"Fresh Super Market botiga xush kelibsiz 👋🏻\n "
                         f"Davom etish uchun tilni tanlang ⤵️", reply_markup=start_inline_keyboard)
    await message.delete()

#
# async def get_menu(message: Message, bot: Bot):
#     await message.answer("Aloooooo", reply_markup=menu_uzb_inline_keyboard)
#

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token, parse_mode='html')


dp = Dispatcher()
dp.message.register(get_start, F.text == '/start')
dp.message.register(set_commands, Command(commands='inline'))
# dp.callback_query.register(get_menu, F.data.startswith('uzb'))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
