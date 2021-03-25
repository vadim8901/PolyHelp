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


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('li', class_='breadcrumb-item active').find_next('span').get_text()
    return str(items)


def parse(teacher_url):
    teacher = ''
    html = get_html(URL + teacher_url)
    if html.status_code == 200:
        teacher = str(get_content(html.text))
    else:
        print("errore!")
    return teacher

