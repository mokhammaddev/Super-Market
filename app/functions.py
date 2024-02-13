import asyncpg
from aiogram import Bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from app.inline import *
from app.commands import set_commands
from app.texts import *
from app.reply import *


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
    simple.clear()
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
    # await call.message.delete()


async def get_cashier(call: CallbackQuery, bot: Bot):
    # CASHIER NAME
    simple.append(1)
    await call.message.answer_photo("https://s-english.ru/images/lilovik-2/kassir5.jpg", vacancy_kassa_text)
    cashier_start_boolean.append(1)
    await call.message.answer(
        f"Pasportingiz bo'yicha familiyangizni ismingizni otasining ismini kiriting (masalan: <b>Falonchiyev Pistonchi Falonchiyevich</b>)",
        reply_markup=information_cashier_keyboard)
    await call.message.delete()


async def get_start_cashier(message: Message):
    # CASHIER AGE
    if len(simple) == 1:
        if list_name == []:
            if 3 <= len(message.text.split()) <= 4:
                list_name.append(message.text)
                await message.answer("Tug'ilgan kuningizni kiriting 📅 (masalan, <b>31.10.2002</b>):")
                simple.append(2)
            # elif 4 < len(message.text.split()) < 3:
            else:
                await message.answer(
                    "Noto'gri kiritildi, iltimos namunadagidek kiriting (masalan: <b>Falonchiyev Pistonchi Falonchiyevich</b>):")

    # CASHIER LOCATION
    # if len(simple) == 2:
    #     if len(list_name) == 1 and list_age == []:
    #         if len(message.text) == 10 and message.text[2] == message.text[5] == '.':
    #             list_age.append(message.text)
    #             await message.answer(
    #                 "Yashash manzili 🏠  viloyat/shahar(tuman)/kocha/raqam-uy (masalan: <b>Sirdaryo/Xovos/17-uy</b> ):")
    #             simple.append(3)
    #         # elif len(list_age) == 1 and list_age == [] and message.text[2] != message.text[5] != '.':
    #         else:
    #             await message.answer("Noto'gri kiritildi, iltimos namunadagidek kiriting 📅 (masalan: 31.10.2002)")
    #
    # # CASHIER PHONE NUMBER
    # if len(simple) == 3 and list_location == [] and len(list_name) == 1:
    #     if len(list_name) == 1 and len(list_age) == 1 and list_location == []:
    #         if len(message.text.split('/')) == 3 and len(message.text) >= 5:
    #             list_location.append(message.text)
    #             await message.answer("Kontakt telefon raqamingizni kiriting 📱 misol: (<b>+998XXXXXXXXXX</b>)",
    #                                  reply_markup=information_cashier_phone_number_keyboard)
    #             simple.append(4)
    #         # elif len(simple) == 3 and list_location == [] and len(list_age) != 1 and len(list_age) != 1:
    #         else:
    #             await message.answer(
    #                 "Noto'gri kiritildi, iltimos namunadagidek kiriting (masalan: <b>Sirdaryo/Xovos/17-uy</b>)")
    #
    # # CASHIER MARRY
    # if len(simple) == 4 and len(list_name) == 1 and len(list_location) >= 1 and list_phone == []:
    #     if len(list_age) == 1 and len(list_location) >= 1:
    #         if message.text[0] == '+' and len(message.text) == 13:
    #             list_phone.append(message.text)
    #             await message.answer("💍 Oilaviy ahvolingiz:", reply_markup=information_cashier_marry_keyboard)
    #             simple.append(5)
    #         else:
    #             await message.answer(
    #                 "Noto'gri kiritildi, iltimos namunadagidek kiriting 📱 misol: (<b>+998XXXXXXXXXX)</b>")

    # CASHIER IS STUDENT
    # if len(simple) == 5 and len(list_name) == 1 and len(
    #         list_location) >= 1 and list_marry == []:
    #     if len(list_marry) == 1 and len(list_phone) == 1:
    # if message.text in ('Oilali', 'Ajrashgan', 'Turmush qurmagan'):
    #     list_marry.append(message.text)
    #     await message.answer("Siz 🎓 talabamisiz?", reply_markup=information_cashier_student_keyboard)
    #     simple.append(6)
    # else:
    #     await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
    #                                  reply_markup=information_cashier_marry_keyboard)

    # CASHIER WORKDAY
    # if len(simple) == 6 and len(list_name) == 1 and len(list_marry) == 1 and len(
    #         list_location) >= 1 and list_is_student == []:
    #     if len(list_marry) == 1 and len(list_phone) == 1:
    #         if message.text in ('Ha talabaman', "Yo'q talaba emasman"):
    #             list_is_student.append(message.text)
    #             await message.answer("💸 Kutilayotgan ish haqi miqdorini ko'rsating (<b>so'm</b>):",
    #                                  reply_markup=information_cashier_price_keyboard)
    #             simple.append(7)
    #         else:
    #             await message.answer("")

    # await message.answer(f"{len(message.text.split('/'))}, {message.text}")

    if message.text in ('Oilali', 'Ajrashgan', 'Turmush qurmagan'):
        list_marry.append(message.text)
        await message.answer("Siz 🎓 talabamisiz?", reply_markup=information_cashier_student_keyboard)
        simple.append(6)
    else:
        await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
                             reply_markup=information_cashier_marry_keyboard)
    print(simple)
    if len(simple) == 3:
        if message.text in ('Ha talabaman', "Yo'q talaba emasman"):
            list_is_student.append(message.text)
            await message.answer("💸 Kutilayotgan ish haqi miqdorini ko'rsating (<b>so'm</b>):",
                                 reply_markup=information_cashier_price_keyboard)
            simple.append(7)

    if len(simple) == 4:
        if message.text == '💵 1-2 million':
            list_price.append(message.text)
            await message.answer("Suratingizni yuboring 🤵 (telefoningizdan selfi olishingiz mumkin)")
            simple.append(8)

    if len(simple) == 5:
        print(message.text, message.photo)
        simple.append(9)
        list_photo.append(message.photo)
        print("list_photo", list_photo)
        await message.answer("Tugatish", answer_markup=list_photo, reply_markup=finish_information_cashier_keyboard)

    if len(simple) == 6:
        await message.answer(f"{list_price}, {list_photo}, {list_name} hammasi shu")


async def anonym_text_delete(message: Message):
    print("Anonymizing text-->", message.text)
    if len(simple) == 0:
        await message.delete()

###############################################################################################################


# # async def cashier_information(message: Message, bot: Bot):
# #     list_cashier_information.append(message.text)
# #     await message.answer(f"{list_cashier_information}")
# #     list_cashier_information.
#
#
# async def cashier_name(message: Message, bot: Bot):
#     if list_name == []:
#         if 3 <= len(message.text.split()) <= 4:
#             list_name.append(message.text)
#             await message.answer("Tug'ilgan kuningizni kiriting 📅 (masalan, 02.11.1995):",
#                                  reply_markup=cashier_name_inline)
#         else:
#             await message.answer(
#                 "Noto'gri kiritildi, iltimos namunadagidek kiriting (masalan: Falonchiyev Pistonchi Falonchiyevich):")
#
#
# async def cashier_age(message: Message):
#     if len(list_name) == 1 and list_age == []:
#         if len(message.text) == 10 and message.text[2] == message.text[5] == '.':
#             list_age.append(message.text)
#             await message.answer(
#                 "Yashash manzili 🏠  viloyat/shahar(tuman)/ko'cha/raqam-uy (masalan: Sirdaryo/Xovos/17-uy):",
#                 reply_markup=cashier_age_inline)
#         else:
#             await message.answer("Noto'gri kiritildi, iltimos namunadagidek kiriting (masalan: 31.10.2002)")
