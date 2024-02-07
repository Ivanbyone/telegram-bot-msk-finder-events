from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def main_menu_buttons() -> ReplyKeyboardMarkup:

    menu = [
        [
            KeyboardButton(text="Перейти в профиль"),
            KeyboardButton(text="Начать поиск мест"),
            KeyboardButton(text="На главную")
        ]
    ]

    menu_keyboard = ReplyKeyboardMarkup(
        keyboard=menu,
        resize_keyboard=True
    )

    return menu_keyboard


async def start_button() -> ReplyKeyboardMarkup:

    start = [
        [
            KeyboardButton(text="Меню")
        ]
    ]

    start_keyboard = ReplyKeyboardMarkup(
        keyboard=start,
        resize_keyboard=True
    )
    
    return start_keyboard


async def location_buttons() -> ReplyKeyboardMarkup:

    loc = [
        [
            KeyboardButton(text="Отправить геолокацию"),
            KeyboardButton(text="Отменить поиск")
        ]
    ]

    loc_keyboard = ReplyKeyboardMarkup(
        keyboard=loc,
        resize_keyboard=True
    )

    return loc_keyboard


# async def go_to_profile() -> ReplyKeyboardMarkup:

#     go_to_profile_button = [
#         [
#             KeyboardButton(text="Перейти в профиль")
#         ]
#     ]

#     keyboard = ReplyKeyboardMarkup(
#         keyboard=go_to_profile_button,
#         resize_keyboard=True
#     )

#     return keyboard
