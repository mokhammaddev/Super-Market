from aiogram.fsm.state import StatesGroup, State


class Vacancy(StatesGroup):
    start = State()
    id = State()
    job = State()
    name = State()
    age = State()
    location = State()
    phone_number = State()
    marry = State()
    is_student = State()
    language = State()
    price = State()
    image = State()
    finish = State()
    menu = State()
