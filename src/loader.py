from aiogram import Bot, Dispatcher
from config import TOKEN
from database import Database

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
data_manager = Database()