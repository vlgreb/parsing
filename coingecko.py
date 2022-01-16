from datetime import datetime

import bs4
from bs4 import BeautifulSoup

from parsing.utils import get_html, save_file

CSV = 'coingecko.csv'

URL = 'https://www.coingecko.com/ru'


def get_content(html):
    """
    :param html:
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.tbody

    currencies = []

    for item in items:
        if not type(item) is bs4.element.NavigableString:
            currencies.append(
                {
                    'title': item.find_all('td')[2].find('a').get_text(strip=True),
                    'price': item.find_all('td')[3].get_text(strip=True),
                    'timestamp': datetime.timestamp(datetime.now()),
                }
            )

    return currencies[:65]


def parser():
    """
    Основной метод
    """
    html = get_html(URL)
    if html.status_code == 200:
        content = get_content(html.content)
        save_file(content, CSV)
        print(f'Парсинг успешно завершен. Результат сохранен в файле {CSV}')
    else:
        print('Error')

parser()
