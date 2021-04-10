#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

URL = 'https://ruz.spbstu.ru'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.100 Safari/537.36',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html, institute):
    url = ''
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('a', class_='faculty-list__link', text=str(institute)).get('href')
    for item in items:
        url += str(item)
    return url


def parse(institute):
    url = ''
    html = get_html(URL)
    if html.status_code == 200:
        url = str(get_content(html.text, institute))
    else:
        print("errore!")
    return URL + url

