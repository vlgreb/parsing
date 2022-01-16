import csv

import requests

from parsing.const import HEADERS


def get_html(url, params=''):
    """
    :param url:
    :param params:
    """
    return requests.get(url, headers=HEADERS, params=params)


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Name', 'Price', 'Timestamp'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['timestamp']])