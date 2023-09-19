from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='uz🇺🇿'),
            KeyboardButton(text='en🇬🇧'),
            KeyboardButton(text='ru🇷🇺'),
        ],
    ],
    resize_keyboard=True
)


keyboards1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏢Biz haqimizda'),
        ],
        [
            KeyboardButton(text='👨‍💻Bosh vakansiyalar'),
            KeyboardButton(text='🗣Yangiliklar'),
        ],
        [
            KeyboardButton(text='☎️Kontakt/Manzil'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)