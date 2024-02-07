from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from configs.config import bot
from markups.markups import main_menu_buttons, start_button, location_buttons
from utils.profile import Profile
from database.database import send_profile

router = Router()


@router.message(F.text.in_(["привет", "Привет"]))
async def hi(message: Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Привет, {message.from_user.full_name}!\n\nНажми /start для начала или продолжения работы с ботом!")
        

@router.message(F.text == "Меню")
async def menu_page(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Выберите дальнейшее действие:",
                           reply_markup=await main_menu_buttons())
    

@router.message(F.text == "Перейти в профиль")
async def go_profile(message: Message) -> None:
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
    

@router.message(F.text == "На главную")
async def go_start(message: Message) -> None:
    await bot.send_message(chat_id=message.from_user.id, 
                               text=f"<b>{message.from_user.full_name}</b>, я Бот по поиску мест и мероприятий, где можно провести время c друзьями или отдохнуть после тяжелого рабочего дня!\n\nМой функционал можно узнать, использовав команду /help",
                               parse_mode='html',
                               reply_markup=await start_button())


@router.message(F.text == "Начать поиск мест")
async def find_places(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                        text="Отправь свою геолокацию, чтобы я поискал места для тебя",
                        parse_mode='html',
                        reply_markup=await location_buttons())
    

@router.message(F.text == "Отменить поиск")
async def cancel_button(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Поиск отменен.\n\nБуду рад тебе помочь снова!",
                           parse_mode="html",
                           reply_markup= await start_button())


@router.message(F.text == "Отправить геолокацию")
async def sending_geolocation(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Updating function...",
                           parse_mode="html",
                           reply_markup=ReplyKeyboardRemove())
    