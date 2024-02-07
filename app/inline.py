from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



menu_uzb_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="E'lonlar",
            callback_data='elon_uzb'
        )
    ],
    [
        InlineKeyboardButton(
            text="❕Biz haqimizda",
            callback_data='biz_haqimizda_uzb'
        ),
        InlineKeyboardButton(
            text="⚙Sozlamalar"
        )
    ],
    [
        InlineKeyboardButton(
            text="📝Tilni o'zgartirish"
        )
    ]
])


start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="O'zbek tili🇺🇿",
            callback_data='uzb',
            reply_markup=menu_uzb_inline_keyboard
        )
    ],
    [
        InlineKeyboardButton(
            text="Rus tili",
            callback_data='rus'
        )
    ],
    [
        InlineKeyboardButton(
            text="Ingliz tili",
            callback_data='eng'
        )
    ]
])
