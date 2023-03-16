from aiogram import executor
import logging
from config import dp
from handlers.basic_handlers import (
    help_command, info_command, picture_command, hello
)
from handlers.shop import send_kb


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(send_kb, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(info_command, commands=["info"])
    dp.register_message_handler(picture_command, commands=["picture"])
    dp.register_message_handler(hello)
    executor.start_polling(dp)
