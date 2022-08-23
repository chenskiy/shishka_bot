from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/help')
        ],
        [
            KeyboardButton(text='/item'),
            KeyboardButton(text='/basket')
        ],
        [
            KeyboardButton(text='/close')
        ]
    ],
    resize_keyboard=True
)

commands_dop_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Корзина')
        ],
        [
            KeyboardButton(text='Показать главное меню')
        ]
    ],
    resize_keyboard=True
)
