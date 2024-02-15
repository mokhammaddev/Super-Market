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

vacancy_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Boshlash")
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
],
    one_time_keyboard=True, resize_keyboard=True,
)

vacancy_phone_number_keyboard = ReplyKeyboardMarkup(keyboard=[
    # [
    #     KeyboardButton(text="Telefon raqam📱", request_contact=True)
    # ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
],
    one_time_keyboard=True, resize_keyboard=True
)

vacancy_marry_keyboard = ReplyKeyboardMarkup(keyboard=[
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

vacancy_student_keyboard = ReplyKeyboardMarkup(keyboard=[
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

vacancy_language_keyboard = ReplyKeyboardMarkup(keyboard=[
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

vacancy_price_keyboard = ReplyKeyboardMarkup(keyboard=[
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

finish_information_vacancy_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Tugatish")
    ],
    [
        KeyboardButton(text="🔼Menyu"),
        KeyboardButton(text="Orqaga↩️")
    ]
], one_time_keyboard=True, resize_keyboard=True)

back_to_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Menyuga qaytish↩")
    ]
], one_time_keyboard=True, resize_keyboard=True)
