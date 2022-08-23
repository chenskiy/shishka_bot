from aiogram import types
from keyboards import X0_callback
from keyboards import start_X0_keyboard, start_callback
from loader import dp


@dp.message_handler(commands=['game'])
async def answer_X0_command(message: types.Message):
    await message.answer(text=f'Игра', reply_markup=start_X0_keyboard)


# @dp.callback_query_handler(start_callback.filter(text=' '))
# async def answer_hod_command(call: types.CallbackQuery):
