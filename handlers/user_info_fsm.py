from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import dp


# FSM - Finite State Mashine
class UserForm(StatesGroup):
    product_id = State()
    name = State()
    age = State()
    address = State()


# async def start_form(message: types.Message):
#     await UserForm.name.set()
#     await message.answer("Как вас зовут?")


async def start_form(callback: types.CallbackQuery):
    await UserForm.product_id.set()
    state = dp.current_state()
    async with state.proxy() as data:
        data['product_id'] = int(callback.data.replace('buy_product_', ''))

    await UserForm.next()
    await callback.message.answer("Как вас зовут?")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await UserForm.next()
    await message.answer("Сколько вам лет?")


async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Пожалуйста, введите возраст цифрами.")
    async with state.proxy() as data:
        data['age'] = int(message.text)  # Сохраняем возраст в данных
    await UserForm.next()  # Переходим к следующему состоянию (адрес)
    await message.answer("Введите ваш адрес")


async def process_address(message: types.Message, state: FSMContext):
    """
        Обработчик ответа на вопрос "Введите ваш адрес"
    """
    kb = types.ReplyKeyboardMarkup()  # кнопки подсказки для дней недели
    kb.add(types.KeyboardButton('Понедельник'),
           types.KeyboardButton('Вторник'), types.KeyboardButton('Среда'),
           types.KeyboardButton('Четверг'), types.KeyboardButton('Пятница'),
           types.KeyboardButton('Субботa'), types.KeyboardButton('Воскресенье'))
    async with state.proxy() as data:
        data['address'] = message.text  # Сохраняем адрес в данных
    await UserForm.next()  # Переходим к следующему состоянию (день недели)
    await message.reply("Выберите день, который вам удобен для получения товара", reply_markup=kb)

    from db.base import create_clients
    async def process_delivery_day(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['delivery_day'] = message.text.strip()  # Сохраняем день в данных
            create_clients(data)
            print(data)
        await message.answer(
            f"Спасибо за заполнение анкеты.\n"
            f"Имя: {data['name']}\n"
            f"Возраст: {data['age']}\n"
            f"Адрес: {data['address']}\n"
            f"День доставки: {data['delivery_day']}")

    await state.finish()  # завершаем состояние
    await message.answer(f"Ваш заказ будет доставлен\nпо адресу: {data['address']} \nдень недели: {data['delivery_day']}")
