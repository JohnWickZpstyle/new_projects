import requests
import json

def get_html(urls):
    response = requests.get(urls)
    return response

def main():

    inp_value = ''.join(input("Введите валютные единицы в сокращенном варианте (EUR,RUB через запятую) "
                              "первое это то что хотите перевести и второе во что хотите перевести, "
                              "нажмите Enter:" ).split(','))

    number_of_cash_units = int(input("Колличество единиц которыое вы имеете: "))

    url = f"https://currate.ru/api/?get=rates&pairs={inp_value},{inp_value}&key=7bb14fda0ea69a44a2244af27297d43a"

    # EURRUB
    ready_currency = round(float(get_html(url).json()['data'][inp_value]) * number_of_cash_units, 3)

    return ready_currency

if __name__ == '__main__':
    print(main())



'''

import requests
import json

def main():

    inp_value = input("Введите валютные единицы в сокращенном варианте (EUR,RUB через запятую) первое это то что хотите"
                      " перевести и второе во что хотите перевести, нажмите Enter:" )
    
    number_of_cash_units = int(input("Колличество единиц которыое вы имеете: "))

    ready_currency = round(float(requests.get(f"https://currate.ru/api/?get=rates&pairs={inp_value},"
                                              f"{inp_value}&key=7bb14fda0ea69a44a2244af27297d43a").json()['data'][
                                     inp_value]) * number_of_cash_units, 3)
    return ready_currency

if __name__ == '__main__':
    main()


'''