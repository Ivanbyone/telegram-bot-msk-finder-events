from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from configs.config import bot

router = Router()


@router.message()
async def other_messages(message: Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"{message.from_user.full_name}, я тебя не понял 🫣\n\nПопробуй написать другое сообщение или нажми /help, чтобы посмотреть, как я могу тебе помочь 😏")
    