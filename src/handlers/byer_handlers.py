from aiogram import types
from loader import dp, bot
from keyboards import start_inline_keyboard, get_basket_inline_keyboard
from aiogram.types import ReplyKeyboardRemove, message
from keyboards import start_callback
from keyboards import commands_default_keyboards
from keyboards import get_item_inline_keyboard
from loader import data_manager
from keyboards import navigation_callback
from keyboards import commands_dop_keyboards
from keyboards import basket_callback


@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет {message.from_user.first_name}!',
                         reply_markup=start_inline_keyboard)


@dp.message_handler(text=['Показать главное меню'])
async def answer_inline_command(message: types.Message):
    await message.answer(text=f'Главное меню', reply_markup=commands_default_keyboards)


@dp.message_handler(commands=['close'])
async def answer_close_command(message: types.Message):
    await message.answer(text=f'Клавиатура убрана', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['basket'])
async def answer_open_command(message: types.Message):
    await message.answer(text=f'Меню', reply_markup=commands_dop_keyboards)


# @dp.message_handler(text=['Корзина'])
# async def answer_open_command(message: types.Message):
#     await message.answer(text=f'Корзина {data_manager.get_item_basket(message.from_user.id)}',
#                          reply_markup=commands_dop_keyboards)
#     item_basket_list = data_manager.get_item_basket(message.from_user.id)
#     for i in item_basket_list:
#         _, item_info = data_manager.get_item(int(i))
#         item_text = f'{item_info["name"]}\n' \
#                     f'{item_info["description"]}\n' \
#                     f'{item_info["count"]}'
#         await message.answer(text=item_text, reply_markup=get_basket_inline_keyboard())

@dp.message_handler(text=['Корзина'])
async def answer_open_command(message: types.Message):
    await message.answer(text=f'Корзина {data_manager.get_basket_inline_keyboard(message.from_user.id)}',
                         reply_markup=commands_dop_keyboards)
    item_basket_list = data_manager.get_basket_inline_keyboard(message.from_user.id)
    for i in item_basket_list:
        status, item_info = data_manager.get_item(int(i))
        item_text = f'{item_info["name"]}\n' \
                    f'{item_info["description"]}\n' \
                    f'{item_info["count"]}'
        await message.answer(text=item_text, reply_markup=get_basket_inline_keyboard())


@dp.callback_query_handler(start_callback.filter())
async def answer_defkey_command(call: types.CallbackQuery):
    await call.message.answer(text='Список команд представлен на клавиатуре', reply_markup=commands_default_keyboards)
    # await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.message_handler(commands=['help'])
async def answer_help_command(message: types.Message):
    await message.answer(text=f'Команда /start вызывает инлайн клавиатуру\n'
                              f'Команда /close закрывает главное меню\n'
                              f'Кнопка "Главное меню" открывает клавиатуру\n'
                              f'Кнопка "item" открывает список инлайн')


@dp.message_handler(commands=['item'])
async def answer_item_command(message: types.Message):
    status, item_info = data_manager.get_item(0)
    item_text = f'{item_info["name"]}\n' \
                f'{item_info["description"]}\n' \
                f'{item_info["count"]}'
    await message.answer(text=item_text, reply_markup=get_item_inline_keyboard())


@dp.callback_query_handler(navigation_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    status, item_info = data_manager.get_item(int(id))
    item_text = f'{item_info["name"]}\n' \
                f'{item_info["description"]}\n' \
                f'{item_info["count"]}'
    await bot.edit_message_text(text=item_text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
    await bot.edit_message_reply_markup(reply_markup=get_item_inline_keyboard(id, status),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)


@dp.callback_query_handler(basket_callback.filter())
async def answer_basket_item(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    data_manager.add_item_basket(item_index=id, user_id=call.from_user.id)


@dp.message_handler()
async def answer_mess_command(message: types.Message):
    print(message.from_user)
    print(message.text)
