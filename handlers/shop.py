from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from config import bot

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Товары',
                           url="https://www.amazon.com/")
ib2 = InlineKeyboardButton(text='адрес',
                           url="https://www.google.com/maps")

ikb.add(ib1, ib2)


async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='HI',
                           reply_markup=ikb)
