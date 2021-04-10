import requests
from bs4 import BeautifulSoup


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.100 Safari/537.36',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def parse(URL):
    html = get_html(URL)
    if html.status_code == 200:
        return False
    if html.status_code == 404:
        return True
