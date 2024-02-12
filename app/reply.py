from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

vacancy_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Kassir 💰"),
        KeyboardButton(text="Farrosh 🧹")
    ],
    [
        KeyboardButton(text="Meva va sabzavotlar sotuvchisi 🤝")
    ],
    [
        KeyboardButton(text="Sotuvchi 🤝"),
        KeyboardButton(text="Yuk Tashuvchi 🚚")
    ],
    [
        KeyboardButton(text="🔼Menyu")
    ]
], one_time_keyboard=True, resize_keyboard=True, selective=True)


menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔼Menyu")
        ]
    ],
    one_time_keyboard=True, resize_keyboard=True, selective=True, is_persistent=True
)


start_cashier = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Orqaga↩️", callback_data="back_1")
    ]
])
