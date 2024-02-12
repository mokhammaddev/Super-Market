from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_inline = InlineKeyboardMarkup(inline_keyboard=[
    [

        InlineKeyboardButton(
            text="O'zbek tili🇺🇿",
            callback_data='uzb'
        ),

        InlineKeyboardButton(
            text="Русский язык🇷🇺",
            callback_data='rus'
        )
    ]
], one_time_keyboard=True)

menu_uzb_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text=" 🎯   V a k a n s i y a   🎯 ",
            callback_data='vacancy'
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
], one_time_keyboard=True)

vacancy_menu_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Kassir 💰", callback_data='kassir'),
        InlineKeyboardButton(text="Farrosh 🧹", callback_data='farrosh')
    ],
    [
        InlineKeyboardButton(text="Meva va sabzavotlar sotuvchisi 🤝", callback_data='meva_sotuvchi')
    ],
    [
        InlineKeyboardButton(text="Sotuvchi 🤝", callback_data='sotuvchi'),
        InlineKeyboardButton(text="Yuk Tashuvchi 🚚", callback_data='yuk_tashuvchi')
    ],
    [
        InlineKeyboardButton(text="🔼Bosh Menyu", callback_data='menu')
    ]
], one_time_keyboard=True)


#############################################################################################################


cashier_start_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Orqaga", callback_data='menu_vacancy'),
        InlineKeyboardButton(text="Kiritish", callback_data='start_cashier')
    ]
], one_time_keyboard=True)

cashier_name_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='cashier_name'),
        InlineKeyboardButton(text='Kiritish', callback_data='cashier_age')
    ]
], one_time_keyboard=True)

cashier_age_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='cashier_age'),
        InlineKeyboardButton(text='Kiritish', callback_data='cashier_location')
    ]
], one_time_keyboard=True)
