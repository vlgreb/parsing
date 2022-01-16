from datetime import datetime

from bs4 import BeautifulSoup

from parsing.utils import get_html, save_file

CSV = 'cryptorank.csv'

URL = 'https://cryptorank.io/'


def get_content(html):
    """
    :param html:
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.tbody

    currencies = []

    for item in items:
        currencies.append(
            {
                'title': item.find_all('td')[1].get_text(),
                'price': item.find_all('td')[2].get_text(),
                'timestamp': datetime.timestamp(datetime.now()),
            }
        )
    return currencies[:3]


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
