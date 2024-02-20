import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import os

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def read_start(messege: Message):
    user_id = messege.from_user.id
    user_full_name = messege.from_user.full_name
    user_name = messege.from_user.first_name
    text = f'Привет {user_name}, напиши мне сообщение на кириллице, и я покажу, что умею!'
    logging.info(f'{user_name} {user_id} запустил бота')

    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_reply(messege: Message):
    user_id = messege.from_user.id
    user_full_name = messege.from_user.full_name
    user_name = messege.from_user.first_name

    cyrillic_to_latin = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': 'ie', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'
    }

    cyrillic_string = messege.text
    latin_string = ''.join(cyrillic_to_latin.get(c, c) for c in cyrillic_string.lower())

    logging.info(f'{user_name} {user_id} {cyrillic_string}')

    await bot.send_message(chat_id=user_id, text=latin_string.title())

if __name__ == '__main__':
    dp.run_polling(bot)