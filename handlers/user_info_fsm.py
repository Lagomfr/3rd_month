from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserForm(StatesGroup):
    name = State()
    age = State()
    address = State()
    delivery_day = State()


async def start_form(message: types.Message):
    await UserForm.name.set()
    await message.answer("Введите ваше имя")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text  
    await UserForm.next()
    await message.answer("Введите ваш возраст")


async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Пожалуйста, введите возраст цифрами.")
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await UserForm.next()
    await message.answer("Введите ваш адрес")


async def process_address(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton('Понедельник'),
           types.KeyboardButton('Вторник'), types.KeyboardButton('Среда'),
           types.KeyboardButton('Четверг'), types.KeyboardButton('Пятница'),
           types.KeyboardButton('Субботa'), types.KeyboardButton('Воскресенье'))
    async with state.proxy() as data:
        data['address'] = message.text
    await UserForm.next()
    await message.reply("Выберите день, который вам удобен для получения товара", reply_markup=kb)


async def process_delivery_day(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['delivery_day'] = message.text.strip()
        print(data)
    await message.answer(
        f"Спасибо за заполнение анкеты.\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Адрес: {data['address']}\n"
        f"День доставки: {data['delivery_day']}")
    await state.finish()
    await message.answer(
        f"Ваш заказ будет доставлен\nпо адресу: {data['address']} \nдень недели: {data['delivery_day']}")
