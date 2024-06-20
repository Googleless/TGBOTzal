from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


goods_amulets_arr = []
goods_runes_arr = []
goods_books_arr = []
goods_cards_arr = []
goods_candles_arr = []


BOT_TOKEN = "7341504754:AAHPS1NXW9IrzWGgGtKeTvTx0p5ooBW1PvY"

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
            KeyboardButton(text="🧝‍Услуги"),
            KeyboardButton(text="🔮Товары"),
            KeyboardButton(text="ℹИнформация"),
        ],
        [
            KeyboardButton(text="В главное меню")
        ]
    ],
    resize_keyboard=True,
    onetime_keyboard=True,
    input_field_placeholder="Выберите желаемое действие"
)

# тут подменю из меню2
# услуги
services_nav_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🪦Порча"),
            KeyboardButton(text="🤔Расклад"),
            KeyboardButton(text="🤍Приворот"),
            KeyboardButton(text="🫠Восковая отливка")
        ],
        [
            KeyboardButton(text="📒Меню")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите услугу"
)

# услуги.порча
porcha_btn  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш эксперт по порчам, Вадим", url='https://t.me/rebdok')
        ]
    ]
)
# услуги.расклад
spread_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш эксперт по раскладам, Ирина", url='https://t.me/velvetali')
        ]
    ]
)
# услуги.приворот
privo_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш эксперт по приворотам, Вадим", url='https://t.me/rebdok')
        ]
    ]
)
# услуги.воск
candle_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш эксперт по восковой отливке, Ирина", url='https://t.me/velvetali')
        ]
    ]
)

# товары навигация
goods_nav_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
              KeyboardButton(text="🧿Амулеты"),
              KeyboardButton(text="♮Руны"),
              KeyboardButton(text="📚Книги"),
              KeyboardButton(text="🃏Карты таро"),
              KeyboardButton(text="🕯️Свечи")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True,
)
goods_amulets_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Клевер Удачи", url='https://ozon.ru/t/Dz7yyPr'),
            InlineKeyboardButton(text="Рунический амулет на процветание и защиту", url='https://ozon.ru/t/AkbRPQ0'),
            InlineKeyboardButton(text="")
        ]
    ]
)
# f[f[f[f[f
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
# кнопка для главного меню
back_to_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="В главное меню")
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
            InlineKeyboardButton(text="⚙Поддержка: ", url='https://t.me/+54jNcQ1e_wsxMzMy'),
            InlineKeyboardButton(text="Написать отзыв: ", url='https://t.me/+54jNcQ1e_wsxMzMy'),
        ]
    ]
)

# подменю ❔
artem = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍺Попов Артём, тестировщик, аналитик", url='https://t.me/praporcshiccc')
        ]
    ]
)
vadim = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌹Абрышкин Вадим, менеджер", url='https://t.me/rebdok')
        ]
    ]
)
irina = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💐Бондарева Ирина, руководитель рабочим процессом", url='https://t.me/velvetali')
        ]
    ]
)
pasha = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚗Вакуленко Павел, разработчик", url='https://t.me/PDKukuruza')
        ]
    ]
)
philip = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔫Землянский Филипп, разработчик", url='https://t.me/Googleless')
        ]
    ]
)
###########################################################################################################


# тут всё для гороскопа:
# инлайны гороскоп стр1
horoscope_kb1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="♈Овен"),
            KeyboardButton(text="♉Телец"),
            KeyboardButton(text="♊Близнецы"),
            KeyboardButton(text="♋Рак"),
            KeyboardButton(text="♌Лев"),
            KeyboardButton(text="♍Дева"),
            KeyboardButton(text="♎Весы"),
            KeyboardButton(text="2"),
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

# инлайны гороскоп стр2
horoscope_kb2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="♏Скорпион"),
            KeyboardButton(text="♐Стрелец"),
            KeyboardButton(text="♑Козерог"),
            KeyboardButton(text="♒Водолей"),
            KeyboardButton(text="♓Рыбы"),
            KeyboardButton(text="1"),
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
###########################################################################################################
