import logging
import aiogram 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(text=['Module vk_bottle not found'])
async def stats(message):
	await message.answer("Напишите в консоли, pip install vk_bottle")

@dp.message_handler(text=['Напишите в консоли, pip install rich'])
async def stats(message):
	await message.answer("Напишите в консоли, pip install rich")
    
@dp.message_handler(text=['DEBUG:urllib3.connectionpool:Starting new HTTPS conection'])
async def stats(message):
	await message.answer("Данная ошибка обозначает что идет созданиие нового HTTPS подлючения, но если после этого ничего не происходит, проверьте валидность ваших аккаунтов в ботнете")    
    

inline_btn_1 = InlineKeyboardButton('➕ Добавить меня в группу', url="http://t.me/PeperHelperBot?startgroup=start")
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

#bot.py
@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    await message.answer(f"<b>👋🏻 Привет, я Pepe Helper! Отвечу на ваши вопросы связанные с установкой ботнета!</b>", parse_mode='html', reply_markup=inline_kb1)

if name == "main":
    executor.start_polling(dp, skip_updates=True)


