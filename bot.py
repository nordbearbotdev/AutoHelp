# Imports
import logging
import aiogram 
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token
bot = Bot(token='')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(text=['Module vk_bottle not found'])
async def stats(message):
	await message.answer("Напишите в консоли, pip install vk_bottle")

@dp.message_handler(text=['Module rich not found'])
async def stats(message):
	await message.answer("Напишите в консоли, pip install rich")
    
@dp.message_handler(text=['DEBUG:urllib3.connectionpool:Starting new HTTPS conection'])
async def stats(message):
	await message.answer("Данная ошибка обозначает что идет созданиие нового HTTPS подлючения, но если после этого ничего не происходит, проверьте валидность ваших аккаунтов в ботнете")    

@dp.message_handler(text=['Termux'])
async def stats(message):
	await message.answer("С недавних пор, у Google поменялась политика в отношении работы с файлами. Поэтому, рекомундую скачивать Termux с F-Droid во избежание ошибок связанных с работой с памятью вашего телефона.")	

inline_btn_1 = InlineKeyboardButton('➕ Добавить меня в группу', url="http://t.me/PeperHelperBot?startgroup=start")
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

#bot.py
@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    await message.answer(f"<b>👋🏻 Привет, я Pepe Helper! Отвечу на ваши вопросы связанные с установкой ботнета!</b>", parse_mode='html', reply_markup=inline_kb1)

@dp.message_handler(commands=['guide'])
async def process_command_1(message: types.Message):
    await message.answer(f"<b>Инструкция как установить ботнет!</b>", parse_mode='html', reply_markup=inline_kb1)

@dp.message_handler(commands=['ping', 'пинг', '.'], commands_prefix=["/", "!"])
async def ping(message: types.Message):
    a = time.time()
    bot_msg = await message.answer(f'<b>⚙️ Проверка пинга....</b>', parse_mode='html')
    if bot_msg:
        b = time.time()
        await bot_msg.edit_text(f'<b>⏱ Пинг: {round((b - a) * 1000)} ms</b>', parse_mode='html')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


