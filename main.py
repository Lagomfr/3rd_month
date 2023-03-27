from aiogram import executor
import logging
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.basic_handlers import (
    start,
    info
)
from handlers.shop import (
    show_categories,
    show_address,
    show_category_flowers
)
from handlers.admin import (
    check_curses,
    pin_message,
    ban_user
)
from handlers.user_info_fsm import (
    start_form,
    process_name,
    process_age,
    process_address,
    UserForm
)
from db.base import (
    init_db,
    delete_table_products,
    create_tables,
    add_products
)


async def startup(_):
    init_db()
    delete_table_products()
    create_tables()
    add_products()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # dp.register_message_handler(start_form, commands=["form"])
    dp.register_callback_query_handler(start_form, lambda callback: callback.data.startswith("buy_product_"))
    dp.register_message_handler(process_name, state=UserForm.name)
    dp.register_message_handler(process_age, state=UserForm.age)
    dp.register_message_handler(process_address, state=UserForm.address)

    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_category_flowers, Text(equals="цветы"))
    dp.register_callback_query_handler(show_address, Text(equals="Адрес"))
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix="!/")
    dp.register_message_handler(ban_user, commands=["да"], commands_prefix="!/")

    # в самом конце
    dp.register_message_handler(check_curses)
    executor.start_polling(dp, on_startup=startup)
