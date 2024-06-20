from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

BOT_TOKEN = "7341504754:AAFpVXDWrVbDCsNrJZNUoWOE5Je4e6KI5jo"

# менюглавное
main_kn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📒Меню"),
            KeyboardButton(text="⚖️Быстрый гороскоп")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие"
)

# подменю из менюглавное
# меню2
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝Услуги"),
            KeyboardButton(text="💵Товары"),
            KeyboardButton(text="❔Информация"),
        ],
        [
            KeyboardButton(text="В главное меню")
        ]
    ],
    resize_keyboard=True,
    onetime_keyboard=True
)

# тут подменю из меню2
# услуги
services_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="😱Порча"),
            KeyboardButton(text="🤔Расклад"),
            KeyboardButton(text="🤍Приворот"),
            KeyboardButton(text="🕺Уворот")
        ],
        [
            KeyboardButton(text="📒Меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# товары
goods_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="placeholder"),
            KeyboardButton(text="placeholder"),
            KeyboardButton(text="placeholder"),
            KeyboardButton(text="placeholder")
        ],
        [
            KeyboardButton(text="📒Меню")
        ]
    ],
    resize_keyboard=True
)

# ❔
info_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜О проекте"),
        ],
        [
            KeyboardButton(text="📒Меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# создаю кнопку для возвращения в меню2 для удобства и использования позже при возможности
simple_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📒Меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# это подменю ❔
inlineinfo_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поддержка: ", url='https://t.me/+54jNcQ1e_wsxMzMy'),
            InlineKeyboardButton(text="Написать отзыв: ", url='https://t.me/+54jNcQ1e_wsxMzMy'),
        ]
    ]
)

# подменю ❔
developers_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌹Абрышкин Вадим, менеджер", url='https://t.me/rebdok'),
            InlineKeyboardButton(text="💐Бондарева Ирина, тимлид", url='https://t.me/velvetali'),
            InlineKeyboardButton(text="🚗Вакуленко Павел, разработчик", url='https://t.me/PDKukuruza'),
            InlineKeyboardButton(text="🔫Землянский Филипп, разработчик", url='https://t.me/Googleless'),
            InlineKeyboardButton(text="🍺Попов Артём, тестировщик, аналитик", url='https://t.me/praporcshiccc')
        ]
    ]
)
###########################################################################################################


# тут всё для гороскопа:
# инлайны гороскоп стр1
horoscope_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="♈Овен", url='https://horo.mail.ru/prediction/aries/today/'),
            InlineKeyboardButton(text="♉Телец", url='https://horo.mail.ru/prediction/taurus/today/'),
            InlineKeyboardButton(text="♊Близнецы", url='https://horo.mail.ru/prediction/gemini/today/'),
            InlineKeyboardButton(text="♋Рак", url='https://horo.mail.ru/prediction/cancer/today/'),
            InlineKeyboardButton(text="♌Лев", url='https://horo.mail.ru/prediction/leo/today/'),
            InlineKeyboardButton(text="♍Дева", url='https://horo.mail.ru/prediction/virgo/today/'),
            InlineKeyboardButton(text="♎Весы", url='https://horo.mail.ru/prediction/libra/today/'),
        ]
    ]
)

# гороскоп переход стр1
reply_kb1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вторая страница гороскопа"),
            KeyboardButton(text="В главное меню")
        ]
    ],
    resize_keyboard=True  # Делаем клавиатуру меньше
)

# инлайны гороскоп стр2
horoscope_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="♏Скорпион", url='https://horo.mail.ru/prediction/scorpio/today/'),
            InlineKeyboardButton(text="♐Стрелец", url='https://horo.mail.ru/prediction/sagittarius/today/'),
            InlineKeyboardButton(text="♑Козерог", url='https://horo.mail.ru/prediction/capricorn/today/'),
            InlineKeyboardButton(text="♒Водолей", url='https://horo.mail.ru/prediction/aquarius/today/'),
            InlineKeyboardButton(text="♓Рыбы", url='https://horo.mail.ru/prediction/pisces/today/'),
        ]
    ]
)

# гороскоп переход стр2
reply_kb2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Первая страница гороскопа"),
            KeyboardButton(text="В главное меню")
        ]
    ],
    resize_keyboard=True  # Делаем клавиатуру меньше
)
###########################################################################################################
