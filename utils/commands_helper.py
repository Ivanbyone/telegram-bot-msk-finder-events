from aiogram.types import BotCommand
from configs.config import bot 

async def set_commands():

    bot_commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/help", description="Посмотреть возможности бота"),
        BotCommand(command="/profile", description="Посмотреть Ваш профиль")
    ]

    await bot.set_my_commands(bot_commands)
