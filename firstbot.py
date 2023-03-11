from aiogram import Bot, Dispatcher, executor, types
import logging
from dotenv import load_dotenv
import os
from random import randint

HELP_COMMAND = """
/start - начать работу с ботом
/help - список всех комманд
/myinfo - информация о пользователе
/photo - отправляет случайную картинку
"""

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def hello(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}")
    await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=["myinfo"])
async def info_command(message: types.Message):
    await message.reply(f'Вас зовут {message.from_user.first_name}\n'
                        f'Ваш id {message.from_user.id}\n'
                        f'Ваш username {message.from_user.username}')


@dp.message_handler(commands=["picture"])
async def picture_command(message: types.Message):
    with open(f"images/{randint(1, 7)}.jpg", 'rb') as img:
        await message.answer_photo(photo=img)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)
