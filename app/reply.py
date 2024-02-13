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


# start_cashier_keyboard = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(text=" ")
#     ]
# ],
#     one_time_keyboard=True, resize_keyboard=True
# )


information_cashier_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
],
    one_time_keyboard=True, resize_keyboard=True
)

information_cashier_phone_number_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Telefon raqam📱", request_contact=True)
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
],
    one_time_keyboard=True, resize_keyboard=True
)

information_cashier_marry_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Oilali"),
        KeyboardButton(text="Ajrashgan")
    ],
    [
        KeyboardButton(text="Turmush qurmagan")
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
],
    one_time_keyboard=True, resize_keyboard=True
)


information_cashier_student_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Ha talabaman"),
        KeyboardButton(text="Yo'q talaba emasman")
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
],
    one_time_keyboard=True, resize_keyboard=True
)


information_cashier_language_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Boshlang'ich"),
        KeyboardButton(text="O'rtacha")
    ],
    [
        KeyboardButton(text="Yuqori"),
        KeyboardButton(text="Master")
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
], one_time_keyboard=True, resize_keyboard=True)


information_cashier_price_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="💵 1-2 million"),
        KeyboardButton(text="💵 2-3 million")
    ],
    [
        KeyboardButton(text="💵 3-4 million"),
        KeyboardButton(text="💵 5-7 million")
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
],
    one_time_keyboard=True, resize_keyboard=True
)

finish_information_cashier_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Tugatish")
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
], one_time_keyboard=True, resize_keyboard=True)

