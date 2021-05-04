import requests
from bs4 import BeautifulSoup



def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    response = requests.get(url, headers=headers)
    html_text = response.text
    return html_text

def get_total_page(html, pam):
    soup = BeautifulSoup(html, 'lxml')
    sorted_mainpage_with_tag = soup.find_all('a', class_="dotted")
    sorted_page_with_price = soup.find_all('div', class_='course')

    return sorted_mainpage_with_tag if pam == 'main page' else sorted_page_with_price

def main():


    convert_money_for_user = []

    for n in range(4):

        url = 'https://kurs.com.ua/#main_table'
        user_inp = input("Введите еюиницу или stop, чтобы выйти ") # Курс доллара


        if user_inp == 'stop':
                break

        how_much_need_to_convert = float(input("Введите количество денежных едниц "))
        main_page = get_total_page(get_html(url), 'main page')

        for text in main_page:
            if text.attrs['title'] == user_inp:
                choice_currency_user = text.attrs['href']
                page_with_price = choice_currency_user



                convert_string_to_number = float(get_total_page(get_html(page_with_price),
                                                                'page with price for user')[0].text[0:5])

                ending_currency_name = ''
                if len(user_inp.split(' ')) == 3:
                    ending_currency_name = user_inp.split(' ')[1:][1][:-1]
                else:
                    ending_currency_name = user_inp.split(' ')[1][:-1]

                convert_money_for_user.append(f"ваш {ending_currency_name} {how_much_need_to_convert} = "
                         f"{convert_string_to_number * how_much_need_to_convert} гривны")



    for currency in convert_money_for_user:
        print(currency)


if __name__ == '__main__':
    main()

