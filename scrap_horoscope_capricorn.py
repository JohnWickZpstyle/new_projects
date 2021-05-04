import requests
from bs4 import BeautifulSoup


url_list = [
            'https://goroskop.i.ua/capricorn/c/',
            'https://orakul.com/horoscope/astrologic/general/capricorn/today.html'
]


response_fst_site, response_second_site = requests.get(url_list[0]), requests.get(url_list[1])


soup_for_fst_site = BeautifulSoup(response_fst_site.text, 'lxml')
soup_for_second_site = BeautifulSoup(response_second_site.text, 'lxml')


horoscope_list = []
goroskop_i_ua = soup_for_fst_site.find_all('ul', class_='multicol multicol-2-fixed')[0].find_all('li', class_='multicol_item')


orakul_com = soup_for_second_site.find_all('div', class_='horoBlock')[0].find_all('p')
formatted_horoscope_from_oracul_com = str(orakul_com[0])[18:-8].strip(' ')


for horoscope in goroskop_i_ua:
    horoscope_day = str(horoscope.find_all('h2'))[5:-6]
    horoscope_forecast = str(horoscope.find_all('p'))[4:-5]
    horoscope = f"{horoscope_day}: \n\t {horoscope_forecast} (Прогноз с сайта https://goroskop.i.ua)"
    horoscope_list.append(horoscope)


horoscope_list.insert(1, f"\t {formatted_horoscope_from_oracul_com}(Прогноз с сайта https://orakul.com/horoscope)")


while True:
        user_input = input('Input day today or tomorrow: ')
        if user_input == 'today':
            print(horoscope_list[0])
            print(horoscope_list[1])
            break
        elif user_input == 'tomorrow':
            print(horoscope_list[2])
            break
        else:
            print("Try again")
            continue
