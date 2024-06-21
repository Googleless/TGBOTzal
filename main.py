import asyncio

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import klava
import zodiacsigns
import developer_info


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
available_pages = ["1", "2"]
###########################################################################################################


# старт бота и главное меню
@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(f"""Добро пожаловать в мир Таро, {message.from_user.first_name}, где символы и архетипы открывают двери в подсознание и тайны Вселенной. Я здесь, чтобы помочь вам найти ответы и понимание с помощью древних карт. Задайте свой вопрос, и давайте вместе раскроем, что звезды готовят для вас.""", reply_markup=klava.main_kn)
    await state.set_state(InMenu.in_menu)
###########################################################################################################


# кнопки главного меню
@dp.message(StateFilter(None, InMenu.in_menu), lambda message: message.text in ["📒Меню", "/menu"])
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Открываем меню... ", reply_markup=klava.menu_kb)
    await state.set_state(InMenu.in_menu)


@dp.message(lambda message: message.text in ["⚖️Быстрый гороскоп", "/horoscope"])
async def send_horoscope(message: types.Message, state: FSMContext):
    await message.answer("Выберите знак зодиака: ", reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)
###########################################################################################################


# кнопки меню:
@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text in ["🧝‍Услуги", "/services"])
async def services(message: types.Message):
    await message.answer("Выберите услугу:", reply_markup=klava.services_nav_kb)


@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text in ["🔮Товары", "/goods"])
async def goods(message: types.Message):
    await message.answer("Выберите товар:", reply_markup=klava.goods_nav_kb)


@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text in ["ℹИнформация", "/info"])
async def info(message: types.Message):
    await message.answer("Показываем наши секреты... ", reply_markup=klava.info_kb)
    await message.answer("Выберите опцию:  ", reply_markup=klava.inlineinfo_kb)


@dp.message(StateFilter(InMenu.in_menu), lambda message: message.text in ["📜О проекте", "/about"])
async def services(message: types.Message):
    await message.answer("Лапочки, работавшие над этим проектом :3 благодарны всем за уделённое им время!!!", reply_markup=klava.simple_menu_kb)
    await message.answer(developer_info.vadim_info, reply_markup=klava.vadim, )
    await message.answer(developer_info.irina_info, reply_markup=klava.irina)
    await message.answer(developer_info.pasha_info, reply_markup=klava.pasha)
    await message.answer(developer_info.philip_info, reply_markup=klava.philip)
    await message.answer(developer_info.artem_info, reply_markup=klava.artem)
###########################################################################################################


# порча💀
@dp.message(lambda message: message.text in ["🪦Порча", "/damage"])
async def porcha(message: types.Message):
    await message.answer("""Негативное воздействие, которое, как считается, может быть наведено на человека, животное или предмет с помощью определенных ритуалов или заклинаний. Это понятие связано с магическими представлениями о том, что негативные мысли или зависть других людей могут причинить вред. Считается, что порча может вызвать различные проблемы, от физических болезней до неудач в личной жизни или бизнесе.Традиционно для снятия порчи используются различные обряды очищения, амулеты и заговоры, которые должны нейтрализовать или отвести негативное влияние.""", reply_markup=klava.porcha_btn)


# расклад🃏
@dp.message(lambda message: message.text in ["🤔Расклад", "/spread"])
async def spread(message: types.Message):
    await message.answer("""Метод гадания, при котором используются специальные карты для получения руководства, понимания скрытых истин или предсказания будущего. Каждая карта Таро имеет свои символы, образы и архетипы, которые могут быть интерпретированы различными способами в зависимости от их расположения и комбинаций с другими картами. Существует множество различных раскладов, и каждый из них предназначен для конкретных вопросов или ситуаций. Например, расклад "Кельтский крест" используется для глубокого понимания сложных ситуаций, в то время как расклад "Три карты" может дать быстрый ответ на конкретный вопрос. Практикующий, или таролог, тщательно тасует карты, задумывая вопрос или держа в уме ситуацию, а затем выкладывает их в определенной последовательности. Каждая позиция в раскладе имеет свое значение, например, прошлое, настоящее, будущее или потенциальные препятствия и ресурсы.""", reply_markup=klava.spread_btn)


# приворот♥
@dp.message(lambda message: message.text in ["🤍Приворот", "/love_spell"])
async def privo(message: types.Message):
    await message.answer("""Магическое воздействие, направленное на привлечение и удержание любви или внимания определенного человека. Это может быть как физическое притяжение, так и эмоциональная связь. Приворот может быть использован для укрепления существующих отношений или для создания новых. Традиционно для приворота используются различные ритуалы и заклинания, которые могут быть выполнены самостоятельно или с помощью гадалки или гадальщика.""", reply_markup=klava.privo_btn)


# воск 🫠
@dp.message(lambda message: message.text in ["🫠Восковая отливка", "/wax_casting"])
async def candle(message: types.Message):
    await message.answer("""Согласно древним целительским практикам восковая отливка служила щитом и отражала от человека все недуги.В наше время, когда медицина на высшем уровне, к технике отливок прибегают, когда происходит цикличность заболеваний без видимых на то причин, или врачи не могут поставить диагноз, а лечение не помогает, происходят абсурдные и необъяснимые стечения обстоятельств, — в этих и многих других случаях не лишним бы сделать отливку и посмотреть первопричину проблемы.Медицина будет лечить последствия, но добраться до истоков не всегда можно с помощью анализов, и тут можно сделать такую энергодиагностику, при этом не исключая сертифицированного медицинского лечения. Восковые отливки — это не панацея от всех бед, но инструмент нетрадиционной помощи и возможность прекратить ненужный форс-мажор в жизни.""", reply_markup=klava.candle_btn)
############################################################################################################


# 🧿Амулеты
@dp.message(lambda message: message.text in ["🧿Амулеты", "/amulets"])
async def amulets(message: types.Message):
    await message.answer("Амулеты, талисманы и обереги - это предметы, помогающие защититься от негатива окружающего мира. в первую очередь. Многие из этих предметов пришли к нам ещё из древних времен, и люди продолжают ими активно пользоваться.", reply_markup=klava.goods_amulets_kb)


# 🪬Руны
@dp.message(lambda message: message.text in ["🪬Руны", "/runes"])
async def runes(message: types.Message):
    await message.answer("""Одним из древнейших методов предсказания обретения мудрости является использование рун — алфавита древних германцев, скандинавов и других народов.
Руны представляют собой не только набор символов, но и глубокую связь с культурой, мифологией и духовностью древних народов.""", reply_markup=klava.goods_runes_kb)


# 📚Книги
@dp.message(lambda message: message.text in ["📚Книги", "/books"])
async def books(message: types.Message):
    await message.answer("Выбор книг, которые можно приобрести в нашем магазине.", reply_markup=klava.goods_books_kb)


# 🃏Карты таро
@dp.message(lambda message: message.text in ["🃏Карты таро", "/cards"])
async def cards(message: types.Message):
    await message.answer("Таро – это система карт, каждая из которых обладает своим значением и помогает лучше понять прошлое, настоящее и будущее.", reply_markup=klava.goods_cards_kb)


# 🕯️Свечи
@dp.message(lambda message: message.text in ["🕯️Свечи", "/candles"])
async def candles(message: types.Message):
    await message.answer("Древняя практика, выдержавшая испытание временем, магия свечей — это мощный метод направления энергии и действий на реализацию ваших желаний. Это было распространено на протяжении веков, становясь все более популярной формой колдовства сегодня.", reply_markup=klava.goods_candles_kb)
############################################################################################################


# кнопка возврата в меню
@dp.message(lambda message: message.text in ["В главное меню", "Назад"])
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer("Возвращаемся в главное меню...  ", reply_markup=klava.main_kn)
    await state.set_state(InMenu.in_menu)


###########################################################################################################


@dp.message(lambda message: message.text in ["♈Овен", "/aries"])
async def aries_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.aries_text()}', reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)


@dp.message(lambda message: message.text in ["♉Телец", "/taurus"])
async def taurus_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.taurus_text()}', reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)


@dp.message(lambda message: message.text in ["♊Близнецы", "/gemini"])
async def gemini_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.gemini_text()}', reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)


@dp.message(lambda message: message.text in ["♋Рак", "/cancer"])
async def cancer_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.cancer_text()}', reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)


@dp.message(lambda message: message.text in ["♌Лев", "/leo"])
async def leo_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.leo_text()}', reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)


@dp.message(lambda message: message.text in ["♍Дева", "/virgo"])
async def virgo_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.virgo_text()}', reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)


@dp.message(lambda message: message.text in ["♎Весы", "/libra"])
async def libra_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.libra_text()}', reply_markup=klava.horoscope_kb1)
    await state.set_state(HoroscopePages.first_page)


@dp.message(lambda message: message.text in ["♏Скорпион", "/scorpio"])
async def scorpio_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.scorpio_text()}', reply_markup=klava.horoscope_kb2)
    await state.set_state(HoroscopePages.second_page)


@dp.message(lambda message: message.text in ["♐Стрелец", "/scorpio"])
async def capricorn_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.sagittarius_text()}', reply_markup=klava.horoscope_kb2)
    await state.set_state(HoroscopePages.second_page)


@dp.message(lambda message: message.text in ["♑Козерог", "/capricorn"])
async def capricorn_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.capricorn_text()}', reply_markup=klava.horoscope_kb2)
    await state.set_state(HoroscopePages.second_page)


@dp.message(lambda message: message.text in ["♒Водолей", "/aquarius"])
async def aquarius_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.aquarius_text()}', reply_markup=klava.horoscope_kb2)
    await state.set_state(HoroscopePages.second_page)


@dp.message(lambda message: message.text in ["♓Рыбы", "/pisces"])
async def pisces_info(message: types.Message, state: FSMContext):
    await message.answer(f'{zodiacsigns.pisces_text()}', reply_markup=klava.horoscope_kb2)
    await state.set_state(HoroscopePages.second_page)


# тут начинается логика гороскопа, идёт проверка на страницы, потом перекидывает
# вроде не ломалось, надо тестировать
@dp.message(
    HoroscopePages.first_page,
    F.text.in_(available_pages))
async def horoscope_pg2(message: Message, state: FSMContext):
    await message.answer("Вторая страница гороскопа", reply_markup=klava.horoscope_kb2)
    await state.set_state(HoroscopePages.second_page)


@dp.message(
    HoroscopePages.second_page,
    F.text.in_(available_pages))
async def horoscope_pg1(message: types.Message, state: FSMContext):
    await state.update_data(page=message.text.lower())
    await message.answer("Первая страница гороскопа", reply_markup=klava.horoscope_kb1,)
    await state.set_state(HoroscopePages.first_page)
###########################################################################################################
# тут заканчивается логика гороскопа
# надо будет дать артёму всё проверить


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
