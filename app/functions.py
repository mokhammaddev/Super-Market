import asyncpg
from aiogram import Bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from app.inline import *
from app.commands import set_commands
from app.texts import *
from app.reply import *

simple = 0
list_name = []
list_age = []
list_location = []
list_phone = []
list_marry = []
list_is_student = []
list_work_day = []


# list_cashier_information = ['FIO', 'date', 'phone', 'marry', 'working time', 'specialty 🎓', 'language', 'price',
#                             'photo']


async def get_text(message: Message):
    await message.answer(f"<b>{message.text}</b>")


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


async def get_kassir(call: CallbackQuery, bot: Bot):
    await call.message.answer_photo("https://s-english.ru/images/lilovik-2/kassir5.jpg", vacancy_kassa_text)
    await call.message.answer(
        "Pasportingiz bo'yicha familiyangizni ismingizni otasining ismini kiriting (masalan: Falonchiyev Pistonchi Falonchiyevich)",
        reply_markup=cashier_start_inline)


# async def cashier_information(message: Message, bot: Bot):
#     list_cashier_information.append(message.text)
#     await message.answer(f"{list_cashier_information}")
#     list_cashier_information.


async def cashier_name(message: Message, bot: Bot):
    if list_name == []:
        if 3 <= len(message.text.split()) <= 4:
            list_name.append(message.text)
            await message.answer("Tug'ilgan kuningizni kiriting 📅 (masalan, 02.11.1995):",
                                 reply_markup=cashier_name_inline)
        else:
            await message.answer(
                "Noto'gri kiritildi, iltimos namunadagidek kiriting (masalan: Falonchiyev Pistonchi Falonchiyevich):")


async def cashier_age(message: Message):
    if len(list_name) == 1 and list_age == []:
        if len(message.text) == 10 and message.text[2] == message.text[5] == '.':
            list_age.append(message.text)
            await message.answer(
                "Yashash manzili 🏠  viloyat/shahar(tuman)/ko'cha/raqam-uy (masalan: Sirdaryo/Xovos/17-uy):",
                reply_markup=cashier_age_inline)
        else:
            await message.answer("Noto'gri kiritildi, iltimos namunadagidek kiriting (masalan: 31.10.2002)")