from aiogram import Bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from app.commands import *
from app.inline import *
from app.reply import *
from app.texts import *
from app.states import *


# id_user = None

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


async def get_settings(call: CallbackQuery):
    await call.answer("Kechirasiz bu sahifa hali tayyor emas")


async def get_about(call: CallbackQuery):
    await call.answer("Kechirasiz bu sahifa hali tayyor emas")


async def get_menu(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
    await call.message.delete()


async def get_vacancies(call: CallbackQuery, bot: Bot):
    if Vacancy.id != call.message.chat.id:
        await call.message.answer("<b>Sizni qiziqtirgan vakansiyani tanlang 💼</b>", reply_markup=vacancy_menu_inline)
    else:
        await call.message.answer("<b>Siz ariza topshirgansiz, qaytatdan ariza topshirasizmi?</b>\n"
                                  "Inlinelardan birini tanlang👇 ",
                                  reply_markup=again_vacancy_inline)
    await call.message.delete()


async def check_vacancy_register(call: CallbackQuery, bot: Bot):
    if Vacancy.id:
        if Vacancy.id == call.message.from_user.id:
            await call.message.answer("Davom ettirish")


async def get_vacancy(call: CallbackQuery, bot: Bot, state: FSMContext):
    if call.data == "cashier":
        await state.update_data(job="Kassir 💰")
        await call.message.answer_photo("https://s-english.ru/images/lilovik-2/kassir5.jpg", vacancy_job_text,
                                        reply_markup=start_vacancy_keyboard)
    if call.data == "cleaner":
        await state.update_data(job="Farrosh 🧹")
        await call.message.answer_photo(
            "https://www.betterteam.com/images/janitor-interview-questions-3210x4815-20201211.jpeg?crop=1:1,smart&width=1200&dpr=2",
            vacancy_job_text, reply_markup=start_vacancy_keyboard)
    if call.data == "fruit_seller":
        await state.update_data(job="Meva va sabzavotlar sotuvchisi 🤝")
        await call.message.answer_photo(
            "https://mir-s3-cdn-cf.behance.net/project_modules/fs/90376b149274795.6303d4039016c.png", vacancy_job_text,
            reply_markup=start_vacancy_keyboard)
    if call.data == "seller":
        await state.update_data(job="Sotuvchi 🤝")
        await call.message.answer_photo(
            "https://www.shutterstock.com/shutterstock/photos/1339855676/display_1500/stock-photo-portrait-of-a-cheese-seller-in-uniform-standing-with-cheese-head-in-the-supermarket-1339855676.jpg",
            vacancy_job_text, reply_markup=start_vacancy_keyboard)
    await state.set_state(Vacancy.start)
    await call.message.delete()


async def get_start_vacancy(message: Message, bot: Bot, state: FSMContext):
    print(message.text)
    if message.text == "Boshlash":
        await message.answer(
            f"Pasportingiz bo'yicha familiyangizni ismingizni otasining ismini kiriting (masalan: <b>Falonchiyev Pistonchi Falonchiyevich</b>)",
            reply_markup=vacancy_keyboard)
        await state.set_state(Vacancy.name)
    else:
        await message.answer("Davom ettirmoqchi bo'lsangiz <b>Boshlash</b> bottomini bosing",
                             reply_markup=start_vacancy_keyboard)


async def get_name_vacancy(message: Message, bot: Bot, state: FSMContext):
    if len(message.text.split()) == 4 or len(message.text.split()) == 3:
        await state.update_data(name=message.text)
        await state.set_state(Vacancy.age)
        await message.answer(f"Tug'ilgan kuningizni kiriting 📅 (masalan, <b>31.10.2002</b>):",
                             reply_markup=vacancy_keyboard)
    elif message.text == "Orqaga↩️":
        await message.answer("Orqaga↩️", reply_markup=start_vacancy_keyboard)
        await message.delete()
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer(
            "Noto'gri kiritildi, iltimos namunadagidek kiriting\n (masalan: <b>Falonchiyev Pistonchi Falonchiyevich</b>):")


async def get_age_vacancy(message: Message, bot: Bot, state: FSMContext):
    if message.text[:2].isdigit() and message.text[3:5].isdigit() and message.text[6:10].isdigit() and len(
            message.text.split('.')) == 3 or len(message.text.split('/')) == 3:
        await state.update_data(age=message.text)
        await message.answer(
            "Yashash manzili 🏠 viloyat/shahar(tuman)/kocha/raqam-uy (masalan: <b>Sirdaryo/Xovos/17-uy</b> ):")
        await state.set_state(Vacancy.location)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.name)
        await message.answer(
            f"Pasportingiz bo'yicha familiyangizni ismingizni otasining ismini kiriting (masalan: <b>Falonchiyev Pistonchi Falonchiyevich</b>)",
            reply_markup=vacancy_keyboard)
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer("Noto'gri kiritildi, iltimos namunadagidek kiriting\n 📅 (masalan: 31.10.2002)")


async def get_location_vacancy(message: Message, bot: Bot, state: FSMContext):
    if len(message.text.split('/')) == 3 or len(message.text.split()) == 3:
        await state.update_data(location=message.text)
        await state.set_state(Vacancy.phone_number)
        await message.answer(
            "Kontakt telefon raqamingizni kiriting 📱 misol: (<b>+998770001732</b> yoki <b>770001732</b>)",
            reply_markup=vacancy_phone_number_keyboard)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.age)
        await message.answer(f"Tug'ilgan kuningizni kiriting 📅 (masalan, <b>31.10.2002</b>):")
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer(
            "Noto'gri kiritildi, iltimos namunadagidek kiriting\n (masalan: <b>Sirdaryo/Xovos/17-uy</b>)")


async def get_phone_number_vacancy(message: Message, bot: Bot, state: FSMContext):
    if (len(message.text) == 13 and message.text[0] == '+' and message.text[1:].isdigit()) or (
            len(message.text) == 9 and message.text.isdigit()):
        await state.update_data(phone_number=message.text)
        await message.answer("💍 Oilaviy ahvolingiz:", reply_markup=vacancy_marry_keyboard)
        await state.set_state(Vacancy.marry)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.location)
        await message.answer(
            "Yashash manzili 🏠 viloyat/shahar(tuman)/kocha/raqam-uy (masalan: <b>Sirdaryo/Xovos/17-uy</b> ):")
        await state.set_state(Vacancy.location)
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer(
            "Noto'gri kiritildi, iltimos namunadagidek kiriting 📱 \nmisol: (<b>+998770001732</b> yoki <b>770001732</b>)",
            reply_markup=vacancy_phone_number_keyboard)


async def get_marry_vacancy(message: Message, bot: Bot, state: FSMContext):
    if message.text in ('Oilali', 'Ajrashgan', 'Turmush qurmagan'):
        await state.update_data(marry=message.text)
        await message.answer("Siz 🎓 talabamisiz?", reply_markup=vacancy_student_keyboard)
        await state.set_state(Vacancy.is_student)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.phone_number)
        await message.answer(
            "Kontakt telefon raqamingizni kiriting 📱 misol: (<b>+998770001732</b> yoki <b>770001732</b>)",
            reply_markup=vacancy_phone_number_keyboard)
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
                             reply_markup=vacancy_marry_keyboard)


async def get_is_student_vacancy(message: Message, bot: Bot, state: FSMContext):
    if message.text in ('Ha talabaman', "Yo'q talaba emasman"):
        await state.update_data(is_student=message.text)
        await message.answer("Rus tilini qanchalik darajada bilasiz? 🇷🇺",
                             reply_markup=vacancy_language_keyboard)
        await state.set_state(Vacancy.language)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.marry)
        await message.answer("💍 Oilaviy ahvolingiz:", reply_markup=vacancy_marry_keyboard)
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
                             reply_markup=vacancy_student_keyboard)


async def get_language_vacancy(message: Message, bot: Bot, state: FSMContext):
    if message.text in ("Boshlang'ich", "O'rtacha", "Yuqori", "Master"):
        await state.update_data(language=message.text)
        await message.answer("💸 Kutilayotgan ish haqi miqdorini ko'rsating (<b>so'm</b>):",
                             reply_markup=vacancy_price_keyboard)
        await state.set_state(Vacancy.price)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.is_student)
        await message.answer("Siz 🎓 talabamisiz?", reply_markup=vacancy_student_keyboard)
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
                             reply_markup=vacancy_language_keyboard)


async def get_price_vacancy(message: Message, bot: Bot, state: FSMContext):
    if message.text in ("💵 1-2 million", "💵 2-3 million", "💵 3-4 million", "💵 5-7 million"):
        await state.update_data(price=message.text)
        await state.update_data(id=message.from_user.id)
        await message.answer("Suratingizni yuboring 🤵 (telefoningizdan selfi olishingiz mumkin)",
                             reply_markup=vacancy_keyboard)
        await state.set_state(Vacancy.image)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.language)
        await message.answer("Rus tilini qanchalik darajada bilasiz? 🇷🇺",
                             reply_markup=vacancy_language_keyboard)
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer("Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash",
                             reply_markup=vacancy_price_keyboard)


async def get_image_vacancy(message: Message, bot: Bot, state: FSMContext):
    if message.photo is not None:
        await state.update_data(image=message.photo)
        await message.answer("Tugatish", reply_markup=finish_information_vacancy_keyboard)
        await state.set_state(Vacancy.finish)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.price)
        await message.answer("💸 Kutilayotgan ish haqi miqdorini ko'rsating (<b>so'm</b>):",
                             reply_markup=vacancy_price_keyboard)
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer("Iltimos rasmingizni yuboring")


async def get_finish_vacancy(message: Message, bot: Bot, state: FSMContext):
    if message.text == "Tugatish":
        data = await state.get_data()
        # Vacancy.id = message.from_user.id
        finish_cashier_information_text = (
            f"<b>Vakansiya💼:</b> {data.get('job')}\n"
            f"<b>Username:</b>@{message.from_user.username}\n"
            f"<b>User id:</b> {data.get('id')}\n"
            f"<b>To'liq ismi:</b> {data.get('name')}\n"
            f"<b>Tug'ilgan sanasi:</b> {data.get('age')} yil\n"
            f"<b>Turar joy manzili:</b> {data.get('location')}\n"
            f"<b>Telefon raqami📱:</b> {data.get('phone_number')}\n"
            f"<b>💍 Oilaviy ahvoli:</b> {data.get('marry')}\n"
            f"<b>Talaba:</b> {data.get('is_student')} ✅\n"
            f"<b>Rus tili darajasi:</b> {data.get('language')}\n"
            f"<b>Kutilayotgan ish haqi darajasi:</b> {data.get('price')}\n"
            f"<b>🤵Asosiy surat:</b> {message.from_user.id} photo\n")
        await bot.send_message(2101536145, f"<b>Yangi ariza</b>\n {finish_cashier_information_text}")
        await message.answer(f"<b>Arizangiz qabul qilindi!</b>", reply_markup=back_to_menu_keyboard)
        await state.set_state(Vacancy.menu)
    elif message.text == "Orqaga↩️":
        await state.set_state(Vacancy.image)
        await message.answer("Suratingizni yuboring 🤵 (telefoningizdan selfi olishingiz mumkin)")
    elif message.text == "🔼Menyu":
        await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
        await message.delete()
    else:
        await message.answer("<b>Noto'gri kiritildi, iltimos pastdagi bottomladan birini tanlash<b>",
                             reply_markup=finish_information_vacancy_keyboard)


async def get_to_menu(message: Message):
    await message.answer("<b>Quyidagilardan birini tanlang</b>", reply_markup=menu_uzb_inline)
