import random

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from configs.config import bot
from markups.markups import start_button
from utils.profile import Profile
from database.database import registraton, validation, send_profile

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:

    start_stickers = [
        r"CAACAgIAAxkBAAELT7Blvrn134vxH3rbovLj7TwGg-5RtgACRQMAArVx2gaTiBAcidwNGzQE",
        r"CAACAgIAAxkBAAELT7dlvr0QUV-K0cDHRSBcDccAAafif74AAvcBAAIWQmsKOfZwb7Rjf8Q0BA",
        r"CAACAgIAAxkBAAELT8llvsPPiy9czTDfQbzcaYWRrHhD9QACrzIAAhnpSEp0UfL43ZZrSTQE",
        r"CAACAgIAAxkBAAELT8VlvsNwIxOQ6loaxw86y1gOnn5pqwAChAADrWW8FEXv16BtLIaKNAQ",
        r"CAACAgIAAxkBAAELT8NlvsNZHmoRsEKo7kIa0Im4hQHVQQAC9Q8AArsgIUjI0a78icEg7jQE",
        r"CAACAgIAAxkBAAELT8FlvsNKSaWvc4-0riuW26zV8-ctjwACTwADrWW8FGuRHI2HrK-TNAQ",
        r"CAACAgIAAxkBAAELT79lvsNEjhj3RS6hQBuj5jdiS3gIbgAC0Q0AAstxcEvO1r8zXvNYlzQE",
        r"CAACAgIAAxkBAAELT71lvsM9l6KxxYF4n6Tw2a3Na1HrzQACggADpsrIDJxaB_KcQQRnNAQ",
        r"CAACAgIAAxkBAAELT7tlvsM3sQWhvo-P-ntgJMffI_9I-AACbwAD9wLID-kz_ZsHgo4yNAQ",
        r"CAACAgIAAxkBAAELT7llvsMxV_5CcFYxCSdEYaEVWKizGQACbgADwDZPE22H7UqzeJmXNAQ"
    ]

    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=random.choice(start_stickers))
    if validation(message.from_user.id) == 0:
        registraton(message.from_user.id, message.from_user.username, message.from_user.full_name)
        await bot.send_message(chat_id=message.from_user.id, 
                               text=f"Привет, <b>{message.from_user.full_name}</b> ✋\nЯ Бот по поиску мест и мероприятий, где можно провести время с друзьями или отдохнуть после тяжелого рабочего дня!\n\nМой функционал можно узнать, использовав команду /help",
                               parse_mode='html',
                               reply_markup=await start_button())
    else:
        await bot.send_message(chat_id=message.from_user.id, 
                               text=f"<b>{message.from_user.full_name}</b>, рад снова тебя видеть!\nПоищем интересные места поблизости?",
                               parse_mode='html',
                               reply_markup=await start_button())


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text="Я <b>Бот</b> для поиска мест, где можно отдохнуть и провести время с друзьями!\n\n<b>Мои базовые команды</b>:\n\n/start - запусти меня и пройди регистрацию,\n/help - узнай мои возможности,\n/profile - посмотри свой профиль.", 
                           parse_mode='html')
    
# need update    
@router.message(Command("profile"))
async def profile(message: Message) -> None:
    db_profile = send_profile(message.from_user.id)
    profile = Profile(db_profile.get("user_id"),
                      db_profile.get("username"),
                      db_profile.get("fullname"),
                      db_profile.get("role"),
                      db_profile.get("attempts"))

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"<b>Мой профиль:</b>\n\n<b>Никнейм</b>: @{profile.username}\n<b>Имя профиля</b>: {profile.fullname}\n<b>Статус</b>: {profile.role}\n<b>Количество доступных поисков</b>: {profile.attempts}",
                           parse_mode='html',
                           reply_markup=await start_button())
    