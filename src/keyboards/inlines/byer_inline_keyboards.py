from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import navigation_callback, del_basket_callback
from .callback_data import start_callback
from .callback_data import basket_callback

# from .callback_data import basket_add_callback

start_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Главое меню',
                                 callback_data=start_callback.new())
        ]
    ]
)


def get_item_inline_keyboard(item_index='0', status='Small'):
    item_inline_keyboard = InlineKeyboardMarkup()
    basket_add = InlineKeyboardButton(text='Добавить в корзину', callback_data=basket_callback.new(id=item_index))
    match status:
        case 'Big':
            index_left = str(int(item_index) - 1)
            btm = InlineKeyboardButton(text='<<<',
                                       callback_data=navigation_callback.new(for_data='items',
                                                                             id=index_left))
            item_inline_keyboard.add(btm)
        case 'Small':
            index_right = str(int(item_index) + 1)
            btm = InlineKeyboardButton(text='>>>',
                                       callback_data=navigation_callback.new(for_data='items',
                                                                             id=index_right))
            item_inline_keyboard.add(btm)
        case _:
            index_left = str(int(item_index) - 1)
            index_right = str(int(item_index) + 1)
            btm_left = InlineKeyboardButton(text='<<<',
                                            callback_data=navigation_callback.new(for_data='items',
                                                                                  id=index_left))
            btm_right = InlineKeyboardButton(text='>>>',
                                             callback_data=navigation_callback.new(for_data='items',
                                                                                   id=index_right))
            item_inline_keyboard.row(btm_left, btm_right)
    item_inline_keyboard.row(basket_add)
    return item_inline_keyboard


def get_basket_inline_keyboard(item_index='0', status='Small'):
    item_inline_basket = InlineKeyboardMarkup()
    basket_del = InlineKeyboardButton(text='Удалить из корзины', callback_data=basket_callback.new(id=item_index))
    match status:
        case 'Big':
            index_left = str(int(item_index) - 1)
            btm = InlineKeyboardButton(text='<<<',
                                       callback_data=navigation_callback.new(for_data='items',
                                                                             id=index_left))
            item_inline_basket.add(btm)
        case 'Small':
            index_right = str(int(item_index) + 1)
            btm = InlineKeyboardButton(text='>>>',
                                       callback_data=navigation_callback.new(for_data='items',
                                                                             id=index_right))
            item_inline_basket.add(btm)
        case _:
            index_left = str(int(item_index) - 1)
            index_right = str(int(item_index) + 1)
            btm_left = InlineKeyboardButton(text='<<<',
                                            callback_data=navigation_callback.new(for_data='items',
                                                                                  id=index_left))
            btm_right = InlineKeyboardButton(text='>>>',
                                             callback_data=navigation_callback.new(for_data='items',
                                                                                   id=index_right))
            item_inline_basket.row(btm_left, btm_right)
    item_inline_basket.row(basket_del)
    return item_inline_basket
