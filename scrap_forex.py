import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    response = requests.get(url, headers=headers)
    html_text = response.text
    return html_text

def get_total_page(html):
    soup = BeautifulSoup(html, 'lxml')
    sorted_html = soup.find('tbody').find_all('td')     # Looking in the body tbody, all tags - td
    return sorted_html

def main():
    url = 'https://ru.investing.com/equities/'

    user_price = input('Please enter price: ')
    number_of_times_stock_checks = ''

    list_with_html_tags, price_list = [], []

    while True:
        try:    # Check the input of the number of times a site search for integer
            number_of_times_stock_checks = int(input("Please, as the number of times to check stocks: "))
        except ValueError:
            print("Please, enter an integer")
            continue
        else:
            break

    count_checks = 0    # site checkout counter

    while count_checks <= number_of_times_stock_checks:
        for link in get_total_page(get_html(url)):
            new_link = str(link).split('-')         # do split('-') on all td tags
            list_with_html_tags.append(new_link)    # Add all these tags to the list.

        for link in list_with_html_tags:
            if link[0] == '<td class="pid':     # If the first element of the list is == '<td class="pid'

                if 'last' in link[2]:           # If 'last' an item is in the same list,
                                                # link == ['<td class="pid', '44465', 'last">1.507,00</td>']

                    link = ''.join(link).split('>')     # We break the list by the tag '>'
                                                        # (['<td class="pid950026last"', '25,22</td', ''])
                    price = link[1].split('<')[0]       # 25,22
                    price_list.append(price)

        count_checks += 1

    if user_price in list(set(price_list)):  # check if the user’s price is listed or not
        print(f'Your stock price is on the stock exchange, and it is: {user_price}')
    else:
        print('such a valuable stock on the stock exchange is not!')


if __name__ == '__main__':
    main()
