from aiogram import types
from db.base import get_products

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(
    types.KeyboardButton("Цветы"),
    types.KeyboardButton("открытки")
)


def keyboard(product_id: int):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("Купить", callback_data=f"buy_product_{product_id}"))
    return kb


async def show_categories(message: types.Message):
    await message.reply("Наши товары", reply_markup=kb)


async def show_category_flowers(message: types.Message):
    i = 0
    for i in range(len(get_products())):
        product = get_products()[i]
        await message.answer(f"""Одежды в наличие:
    Название: {product[1]}
    Описание: {product[2]}
    Цена: {product[3]} {product[4]}
    {product[5]}""", reply_markup=keyboard(product[0]))


async def show_address(message: types.Message):
    await message.answer("г.Бишкек, ул.Ибраимова 103")
