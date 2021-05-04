'''
valutnie_pari = requests.get(" https://currate.ru/api/?get=currency_list&key=7bb14fda0ea69a44a2244af27297d43a")


{'status': '200', 'message': 'currency_list', 'data': ['BCHEUR', 'BCHGBP', 'BCHJPY', 'BCHRUB', 'BCHUSD', 'BCHXRP',
'BTCBCH', 'BTCEUR', 'BTCGBP', 'BTCJPY', 'BTCRUB', 'BTCUSD', 'BTCXRP', 'BTGUSD', 'BYNRUB', 'CADRUB', 'CHFRUB', 'CNYEUR',
'CNYRUB', 'CNYUSD', 'ETHEUR', 'ETHGBP', 'ETHJPY', 'ETHRUB', 'ETHUSD', 'EURAED', 'EURAMD', 'EURBGN', 'EURBYN', 'EURGBP',
'EURJPY', 'EURKZT', 'EURRUB', 'EURTRY', 'EURUSD', 'GBPAUD', 'GBPBYN', 'GBPJPY', 'GBPRUB', 'GELRUB', 'GELUSD', 'IDRUSD', '
JPYAMD', 'JPYAZN', 'JPYRUB', 'LKREUR', 'LKRRUB', 'LKRUSD', 'MDLEUR', 'MDLRUB', 'MDLUSD', 'MMKEUR', 'MMKRUB', 'MMKUSD', '
RSDEUR', 'RSDRUB', 'RSDUSD', 'RUBAED', 'RUBAMD', 'RUBAUD', 'RUBBGN', 'RUBKZT', 'RUBMYR', 'RUBNZD', 'RUBSGD', 'RUBTRY', '
RUBUAH', 'THBCNY', 'THBEUR', 'THBRUB', 'USDAED', 'USDAMD', 'USDAUD', 'USDBGN', 'USDBYN', 'USDCAD', 'USDGBP', 'USDILS',
'USDJPY', 'USDKGS', 'USDKZT', 'USDMYR', 'USDRUB', 'USDTHB', 'USDUAH', 'USDVND', 'XRPEUR', 'XRPGBP', 'XRPJPY', 'XRPRUB',
 'XRPUSD', 'ZECUSD']}
{'status': 200, 'message': 'rates', 'data': {'USDRUB': '64.1824'}}

inp_value = "".join('USDRUB'.split(","))


valuta =  round(float({'status': 200, 'message': 'rates', 'data': {'USDRUB': '64.1824'}}['data'][inp_value]) * 10, 3)

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