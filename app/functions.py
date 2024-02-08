from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from app.inline import start_inline_keyboard, menu_uzb_inline_keyboard
from app.commands import set_commands


async def get_start(message: Message, bot: Bot):
    await set_commands(bot)
    await message.answer(f"Davom etish uchun tilni tanlang \n"
                         f"Выберите язык, чтобы продолжить \n"
                         f"Choose a language to continue \n", reply_markup=start_inline_keyboard)
    await message.delete()


async def get_again_start(call: CallbackQuery, bot: Bot):
    await set_commands(bot)
    await call.message.answer(f"Qaytatdan davom etish uchun tilni tanlang \n\n"
                              f"Пожалуйста, выберите язык, чтобы продолжить снова \n\n"
                              f"Please select a language to continue again \n\n",
                              reply_markup=start_inline_keyboard)
    await call.message.delete()


async def get_english_start(message: Message, bot: Bot):
    await message.answer("Bu til hali rivojlanmagan")


async def get_menu(call: CallbackQuery, bot: Bot):
    await call.message.answer("Davom Etish", reply_markup=menu_uzb_inline_keyboard)
    await call.message.delete()

