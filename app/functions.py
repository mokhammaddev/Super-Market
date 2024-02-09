import asyncpg
from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from app.inline import *
from app.commands import set_commands
from app.texts import *
from app.reply import *


async def create_pool():
    return await asyncpg.create_pool(user="abdulloh", password="00373", host="localhost", database="market",
                                     command_timeout=60)


async def get_start(message: Message, bot: Bot):
    await set_commands(bot)
    await message.answer(f"Davom etish uchun tilni tanlang \n"
                         f"Выберите язык, чтобы продолжить \n", reply_markup=start_inline)
    await message.delete()


async def get_again_start(call: CallbackQuery, bot: Bot):
    await set_commands(bot)
    await call.message.answer(f"Qaytatdan davom etish uchun tilni tanlang \n\n"
                              f"Пожалуйста, выберите язык, чтобы продолжить снова \n\n",
                              reply_markup=start_inline)
    await call.message.delete()


"""Uzbek"""


async def get_vacancies(call: CallbackQuery, bot: Bot):
    await call.message.answer("<b>Sizni qiziqtirgan vakansiyani tanlang 💼</b>", reply_markup=vacancy_menu_inline)
    await call.message.delete()


async def get_menu(call: CallbackQuery, bot: Bot):
    await call.message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
    await call.message.delete()


async def get_kassir(message: Message, bot: Bot):
    await message.answer_photo("https://s-english.ru/images/lilovik-2/kassir5.jpg", vacancy_kassa_text)
    await message.answer(
        "Pasportingiz bo'yicha familiyangizni ismingizni otasining ismini kiriting (masalan: Falonchiyev Pistonchi Falonchiyevich)",
        reply_markup=menu_keyboard)
