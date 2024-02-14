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
    await call.message.delete()


async def get_cashier(call: CallbackQuery, bot: Bot):
    # CASHIER NAME
    simple.append(1)
    await call.message.answer_photo("https://s-english.ru/images/lilovik-2/kassir5.jpg", vacancy_cashier_text)
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
            else:
                await message.answer(
                    "Noto'gri kiritildi, iltimos namunadagidek kiriting\n (masalan: <b>Falonchiyev Pistonchi Falonchiyevich</b>):")

    # CASHIER LOCATION
    if len(simple) == 2:
        if len(list_name) == 1 and list_age == []:
            if len(message.text) == 10 and message.text[2] == message.text[5] == '.':
                list_age.append(message.text)
                await message.answer(
                    "Yashash manzili 🏠  viloyat/shahar(tuman)/kocha/raqam-uy (masalan: <b>Sirdaryo/Xovos/17-uy</b> ):")
                simple.append(3)
            # else:
            #     if len(message.text) != 10:
            #         await message.answer("Noto'gri kiritildi, iltimos namunadagidek kiriting\n 📅 (masalan: 31.10.2002)")

    # CASHIER PHONE NUMBER
    if len(simple) == 3 and list_location == [] and len(list_name) == 1:
        if len(list_name) == 1 and len(list_age) == 1 and list_location == []:
            if len(message.text.split('/')) == 3 and len(message.text) >= 5:
                list_location.append(message.text)
                await message.answer("Kontakt telefon raqamingizni kiriting 📱 misol: (<b>+998XXXXXXXXXX</b>)",
                                     reply_markup=information_cashier_phone_number_keyboard)
                simple.append(4)
            else:
                if len(message.text.split('/')) != 3 and len(message.text) < 5:
                    await message.answer(
                        "Noto'gri kiritildi, iltimos namunadagidek kiriting\n (masalan: <b>Sirdaryo/Xovos/17-uy</b>)")

    # CASHIER MARRY
    if len(simple) == 4 and len(list_name) == 1 and len(list_location) >= 1 and list_phone == []:
        if len(list_age) == 1 and len(list_location) >= 1:
            if message.text[0] == '+' and len(message.text) == 13:
                list_phone.append(message.text)
                await message.answer("💍 Oilaviy ahvolingiz:", reply_markup=information_cashier_marry_keyboard)
                simple.append(5)
            # else:
            #     if message.text[0] != '+' and len(message.text) != 13:
            #         await message.answer(
            #             "Noto'gri kiritildi, iltimos namunadagidek kiriting 📱 \nmisol: (<b>+998XXXXXXXXXX)</b>")

    # CASHIER IS STUDENT
    if len(simple) == 5 and len(list_name) == 1 and len(list_location) >= 1 and list_marry == []:
        if len(list_phone) == 1:
            if message.text in ('Oilali', 'Ajrashgan', 'Turmush qurmagan'):
                list_marry.append(message.text)
                await message.answer("Siz 🎓 talabamisiz?", reply_markup=information_cashier_student_keyboard)
                simple.append(6)
            # else:
            #     await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
            #                          reply_markup=information_cashier_marry_keyboard)

    # CASHIER LANGUAGE
    if len(simple) == 6 and len(list_name) == 1 and len(list_marry) == 1 and len(
            list_location) >= 1 and list_is_student == []:
        if len(list_marry) == 1 and len(list_phone) == 1:
            if message.text in ('Ha talabaman', "Yo'q talaba emasman"):
                list_is_student.append(message.text)
                await message.answer("Rus tilini qanchalik darajada bilasiz? 🇷🇺",
                                     reply_markup=information_cashier_language_keyboard)
                simple.append(7)
            # else:
            #     await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
            #                          reply_markup=information_cashier_student_keyboard)

    # CASHIER PRICE
    if len(simple) == 7 and len(list_name) == 1 and len(list_marry) == 1 and len(
            list_location) >= 1 and list_language == []:
        if len(list_marry) == 1 and len(list_phone) == 1:
            if message.text in ("Boshlang'ich", "O'rtacha", "Yuqori", "Master"):
                list_language.append(message.text)
                await message.answer("💸 Kutilayotgan ish haqi miqdorini ko'rsating (<b>so'm</b>):",
                                     reply_markup=information_cashier_price_keyboard)
                simple.append(8)
            # else:
            #     await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
            #                          reply_markup=information_cashier_language_keyboard)

    # CASHIER PHOTO
    if len(simple) == 8 and len(list_name) == 1 and len(list_marry) == 1 and len(
            list_location) >= 1 and list_price == []:
        if len(list_is_student) == 1 and len(list_marry) == 1:
            if message.text in ("💵 1-2 million", "💵 2-3 million", "💵 3-4 million", "💵 5-7 million"):
                list_price.append(message.text)
                await message.answer("Suratingizni yuboring 🤵 (telefoningizdan selfi olishingiz mumkin)")
                simple.append(9)
            # else:
            #     await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
            #                          reply_markup=information_cashier_price_keyboard)

    # CASHIER FINISH INFORMATION

    if len(simple) == 9 and len(list_name) == 1 and len(list_marry) == 1 and list_photo == []:
        if len(list_is_student) == 1 and len(list_price) == 1:
            if message.photo is not None:
                list_photo.append(message.photo)
                await message.answer("Tugatish", reply_markup=finish_information_cashier_keyboard)
                simple.append(10)
            else:
                await message.answer("Iltimos rasmingizni yuboring")

    if len(simple) == 10:
        if message.text == "Tugatish":
            finish_cashier_information_text = (
                f"<b>Vakansiya💼:</b> Cashier\n"
                f"<b>To'liq ismi:</b> {list_name[0]}\n"
                f"<b>Tug'ilgan sanasi:</b> {list_age[0]} yil\n"
                f"<b>Turar joy manzili:</b> {list_location[0]}\n"
                f"<b>Telefon raqami📱:</b> {list_phone[0]}\n"
                f"<b>💍 Oilaviy ahvoli:</b> {list_marry[0]}\n"
                f"<b>Talaba:</b> {list_is_student[0]} ✅\n"
                f"<b>Rus tili darajasi:</b> {list_language[0]}\n"
                f"<b>Kutilayotgan ish haqi darajasi:</b> {list_price[0]}\n"
                f"<b>🤵Asosiy surat:</b> photo\n"
                f"<b>Shaxsiy ma'lumotlar:</b> ✔️ Roziman\n"
            )
            print(finish_cashier_information_text)
            simple.append(11)
            await message.answer(f"{finish_cashier_information_text}", reply_markup=back_to_menu)

    if len(simple) == 11:
        if message.text == "Menuga qaytish↩":
            await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)


async def anonym_text_delete(message: Message):
    print("Anonymizing text-->", message.text)
    if len(simple) == 0:
        await message.delete()
