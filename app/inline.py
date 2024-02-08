from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [

        InlineKeyboardButton(
            text="O'zbek tili🇺🇿",
            callback_data='uzb'
        )
    ],
    [
        InlineKeyboardButton(
            text="Русский язык🇷🇺",
            callback_data='rus'
        )],
    [
        InlineKeyboardButton(
            text="English language🇺🇸",
            callback_data='eng'
        )
    ]
])

menu_uzb_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text=" 🎯   V a k a n s i y a   🎯 ",
            callback_data='elon_uzb'
        )
    ],
    [
        InlineKeyboardButton(
            text="❕Biz haqimizda",
            callback_data='about_uzb'
        ),
        InlineKeyboardButton(
            text="⚙Sozlamalar",
            callback_data='settings_uzb'
        )
    ],
    [
        InlineKeyboardButton(
            text="📝Tilni o'zgartirish",
            callback_data='edit_language'
        )
    ]
])
