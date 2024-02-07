import asyncio
import logging

from configs.config import bot, dp
from handlers import messages_from_user, unmarked_messages
from handlers.all_users_commands import commands
from utils.commands_helper import set_commands
from handlers.admin_commands import admin_commands


async def main() -> None:
    dp.include_routers(
        admin_commands.router,
        commands.router,
        messages_from_user.router,
        unmarked_messages.router
    )

    dp.startup.register(set_commands)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, 
                        filename="bot_logs.log", 
                        filemode="w",
                        format="%(asctime)s  %(levelname)s %(message)s")
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, 
            SystemError, 
            SystemExit, 
            ImportError):
        logging.info("Bot stopped!")
