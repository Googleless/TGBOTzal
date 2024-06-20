from bs4 import BeautifulSoup

import requests

# этот скрипт содержит знаки зодиака и их обработку, не трахаться с кодом без филиппа!!!!!!


url_aries = 'https://horo.mail.ru/prediction/aries/today/'
url_taurus = 'https://horo.mail.ru/prediction/taurus/today/'
url_gemini = 'https://horo.mail.ru/prediction/gemini/today/'
url_cancer = 'https://horo.mail.ru/prediction/cancer/today/'
url_leo = 'https://horo.mail.ru/prediction/leo/today/'
url_virgo = 'https://horo.mail.ru/prediction/virgo/today/'
url_libra = 'https://horo.mail.ru/prediction/libra/today/'
url_scorpio = 'https://horo.mail.ru/prediction/scorpio/today/'
url_sagittarius = 'https://horo.mail.ru/prediction/sagittarius/today/'
url_capricorn = 'https://horo.mail.ru/prediction/capricorn/today/'
url_aquarius = 'https://horo.mail.ru/prediction/aquarius/today/'
url_pisces = 'https://horo.mail.ru/prediction/pisces/today/'


# я гений
# овен
def aries_text():
    response_aries = requests.get(url_aries)
    data_aries = response_aries.text
    soup_aries = BeautifulSoup(data_aries, 'html.parser')
    divs_aries = soup_aries.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_aries:
        return div.get_text()


# телец
def taurus_text():
    response_taurus = requests.get(url_taurus)
    data_taurus = response_taurus.text
    soup_taurus = BeautifulSoup(data_taurus,  'html.parser')
    divs_taurus = soup_taurus.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_taurus:
        return div.get_text()


# близнецы
def gemini_text():
    response_gemini = requests.get(url_gemini)
    data_gemini = response_gemini.text
    soup_gemini = BeautifulSoup(data_gemini,   'html.parser')
    divs_gemini = soup_gemini.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_gemini:
        return div.get_text()


# рак
def cancer_text():
    response_cancer = requests.get(url_cancer)
    data_cancer = response_cancer.text
    soup_cancer = BeautifulSoup(data_cancer, 'html.parser')
    divs_cancer = soup_cancer.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_cancer:
        return div.get_text()


# лев
def leo_text():
    response_leo = requests.get(url_leo)
    data_leo = response_leo.text
    soup_leo = BeautifulSoup(data_leo, 'html.parser')
    divs_leo = soup_leo.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_leo:
        return div.get_text()


# дева
def virgo_text():
    response_virgo = requests.get(url_virgo)
    data_virgo = response_virgo.text
    soup_virgo = BeautifulSoup(data_virgo, 'html.parser')
    divs_virgo = soup_virgo.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_virgo:
        return div.get_text()


# весы
def libra_text():
    response_libra = requests.get(url_libra)
    data_libra = response_libra.text
    soup_libra = BeautifulSoup(data_libra, 'html.parser')
    divs_libra = soup_libra.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_libra:
        return div.get_text()


# скорпион
def scorpio_text():
    response_scorpio = requests.get(url_scorpio)
    data_scorpio = response_scorpio.text
    soup_scorpio = BeautifulSoup(data_scorpio, 'html.parser')
    divs_scorpio = soup_scorpio.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_scorpio:
        return div.get_text()


# стрелец
def sagittarius_text():
    response_sagittarius = requests.get(url_sagittarius)
    data_sagittarius = response_sagittarius.text
    soup_sagittarius = BeautifulSoup(data_sagittarius,   'html.parser')
    divs_sagittarius = soup_sagittarius.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_sagittarius:
        return div.get_text()


# козерог
def capricorn_text():
    response_capricorn = requests.get(url_capricorn)
    data_capricorn = response_capricorn.text
    soup_capricorn = BeautifulSoup(data_capricorn, 'html.parser')
    divs_capricorn = soup_capricorn.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_capricorn:
        return div.get_text()


# водолей
def aquarius_text():
    response_aquarius = requests.get(url_aquarius)
    data_aquarius = response_aquarius.text
    soup_aquarius = BeautifulSoup(data_aquarius, 'html.parser')
    divs_aquarius = soup_aquarius.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_aquarius:
        return div.get_text()


# рыбы
def pisces_text():
    response_pisces = requests.get(url_pisces)
    data_pisces = response_pisces.text
    soup_pisces = BeautifulSoup(data_pisces, 'html.parser')
    divs_pisces = soup_pisces.find_all('div', class_='article__item article__item_alignment_left article__item_html')
    for div in divs_pisces:
        return div.get_text()
