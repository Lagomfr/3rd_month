from aiogram import types


async def example(message: types.Message):
    # print(message.chat.type)
    if message.chat.type != 'private':
        print(message.text)
        admins = await message.chat.get_administrators()
        for a in admins:
            print(a["user"]["username"])
        await message.answer("Привет")


async def check_curses(message: types.Message):
    bad_words = ["дурак", "собака"]
    if message.chat.type != 'private':
        for word in bad_words:
            if word in message.text.lower().replace(' ', ''):
                print(message.text.lower().replace(' ', ''))
                # await message.reply("Не ругайся")
                await message.reply(f"Админы, забанить этого пользователя за мат?[{message.from_user.id}]")
                break


async def pin_message(message: types.Message):
    if message.chat.type != 'private':
        print(message.text)
        if message.reply_to_message:
            await message.reply_to_message.pin()


async def is_admin(message: types.Message) -> bool:
    author_id = message.from_user.id
    admins = await message.chat.get_administrators()
    print(admins)
    for adm in admins:
        if author_id == adm['user']['id']:
            return True

    return False


async def ban_user(message: types.Message):
    author_admin = await is_admin(message)
    if message.chat.type != 'private':
        if message.reply_to_message and author_admin:
            # await message.bot.ban_chat_member(
            #     chat_id= message.chat.id,
            #     user_id= message.reply_to_message.from_user.id
            # )
            await message.answer("Забанил юзера {message.reply_to_message.from_user.username}")