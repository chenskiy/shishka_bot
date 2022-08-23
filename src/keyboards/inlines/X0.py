from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .callback_data import X0_callback

start_X0_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new()),
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new()),
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new())
        ],
        [
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new()),
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new()),
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new())
        ],
        [
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new()),
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new()),
            InlineKeyboardButton(text=' ',
                                 callback_data=X0_callback.new())
        ]
    ]
)
