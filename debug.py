from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from bs4 import BeautifulSoup

import requests


url_aries = 'https://horo.mail.ru/prediction/aries/today/'

response_aries = requests.get(url_aries)

data_aries = response_aries.text

soup_aries = BeautifulSoup(data_aries, 'html.parser')

divs_aries = soup_aries.find_all('div', class_='article__item article__item_alignment_left article__item_html')


def parse_aries(divs_aries):
    for div in divs_aries:
        print(div.get_text())


parse_aries(divs_aries)


mainmenunewsupport = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(f'{cfg['button_new_question']}')
        ]
    ]
)


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