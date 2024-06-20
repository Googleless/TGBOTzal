import asyncio

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import klava

bot = Bot(token=klava.BOT_TOKEN)

dp = Dispatcher()


# статус пользователя по страницам гороскопа
class HoroscopePages(StatesGroup):
    first_page = State()
    second_page = State()


# статус пользователя по меню
class InMenu(StatesGroup):
    in_menu = State()
    not_in_menu = State()


# массив страниц пользователя, я незнаю если это работает, но удалять не хочу
available_pages = ["Первая страница гороскопа", "Вторая страница гороскопа"]
###########################################################################################################


# старт бота и главное меню
@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}!", reply_markup=klava.main_kn)
    await state.set_state(InMenu.in_menu)
###########################################################################################################


# кнопки главного меню
@dp.message(StateFilter(None, InMenu.in_menu), lambda message: message.text == "📒Меню")
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Открываем меню... ", reply_markup=klava.menu_kb)
    await state.set_state(InMenu.in_menu)


@dp.message(lambda message: message.text == "⚖️Быстрый гороскоп")
async def send_horoscope(message: types.Message, state: FSMContext):
    await message.answer("Открываем гороскоп... ", reply_markup=klava.reply_kb1)
    await message.answer("Выберите знак зодиака: ", reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)
###########################################################################################################


# кнопки меню:
@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text == "📝Услуги")
async def services(message: types.Message):
    await message.answer("Выберите услугу:", reply_markup=klava.services_kb)


@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text == "💵Товары")
async def goods(message: types.Message):
    await message.answer("Показываем товары...", reply_markup=klava.goods_kb)
    await message.answer("Выберите товар: ", reply_markup=klava.simple_goods_kb)


@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text == "❔Информация")
async def info(message: types.Message):
    await message.answer("Показываем наши секреты... ", reply_markup=klava.info_kb)
    await message.answer("Выберите опцию:  ", reply_markup=klava.inlineinfo_kb)


@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text == "📜О проекте")
async def services(message: types.Message):
    await message.answer("Лапочки, работавшие над этим проектом :3", reply_markup=klava.developers_kb)
    await message.answer("Спасибо за использование бота!", reply_markup=klava.simple_menu_kb)
###########################################################################################################


# кнопка возврата в меню
@dp.message(lambda message: message.text == "В главное меню")
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Возвращаемся в главное меню...  ", reply_markup=klava.main_kn)
    await state.set_state(InMenu.in_menu)
###########################################################################################################


# тут начинается логика гороскопа, идёт проверка на страницы, потом перекидывает
# вроде не ломалось, надо тестировать
@dp.message(
    HoroscopePages.first_page,
    F.text.in_(available_pages))
async def horoscope_pg2(message: Message, state: FSMContext):
    await message.answer("Вторая страница гороскопа", reply_markup=klava.horoscope_kb2)
    await message.answer("Выберите знак зодиака: ", reply_markup=klava.reply_kb2)
    await state.set_state(HoroscopePages.second_page)


@dp.message(
    HoroscopePages.second_page,
    F.text.in_(available_pages))
async def horoscope_pg1(message: types.Message, state: FSMContext):
    await state.update_data(page=message.text.lower())
    await message.answer("Первая страница гороскопа", reply_markup=klava.horoscope_kb1,)
    await message.answer("Выберите знак зодиака: ", reply_markup=klava.reply_kb1)
    await state.set_state(HoroscopePages.first_page)
###########################################################################################################
# тут заканчивается логика гороскопа
# надо будет дать артёму всё проверить


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
