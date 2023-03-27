from aiogram import types
from random import randint

HELP_COMMAND = """
/start - начать работу с ботом
/help - список всех комманд
/myinfo - информация о пользователе
/photo - отправляет случайную картинку
"""


async def start(message: types.Message):
    """Функция, которая обрабатывает команду /start"""
    # await message.answer("Привет")
    await message.reply("Я - бот Python273.")
    await message.delete()


# @dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


# @dp.message_handler(commands=["myinfo"])
async def info(message: types.Message):
    """Ф-я которая обрабатывает команду info
    и отправляет юзеру его никнеймом"""
    await message.reply(f"Ты - {message.from_user.username}")


# @dp.message_handler(commands=["picture"])
async def picture_command(message: types.Message):
    with open(f"images/{randint(1, 7)}.jpg", 'rb') as img:
        await message.answer_photo(photo=img)


async def hello(message: types.Message):
    await message.answer('Hello!)')
