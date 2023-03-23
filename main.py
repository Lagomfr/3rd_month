from aiogram import executor
import logging
from config import dp
from handlers.basic_handlers import (
    help_command, info_command, picture_command, hello
)
from handlers.shop import send_kb
from handlers.admin import check_curses, ban_user
from handlers.user_info_fsm import (start_form, process_name, process_age,
                                    process_address, UserForm, process_delivery_day)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(send_kb, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(info_command, commands=["info"])
    dp.register_message_handler(picture_command, commands=["picture"])
    dp.register_message_handler(hello)
    dp.register_message_handler(ban_user, commands=["да"], commands_prefix=['/'])
    dp.register_message_handler(start_form, commands=["form"])
    dp.register_message_handler(process_name, state=UserForm.name)
    dp.register_message_handler(process_age, state=UserForm.age)
    dp.register_message_handler(process_address, state=UserForm.address)
    dp.register_message_handler(process_delivery_day, state=UserForm.delivery_day)
    dp.register_message_handler(check_curses)

    executor.start_polling(dp)
