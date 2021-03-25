#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from Schedule_parse import Institute_parser

URL = str(Institute_parser.parse("Институт компьютерных наук и технологий") + "/")


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.100 Safari/537.36',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html, group_number):
    url = ''
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('a', class_='groups-list__link', text=group_number).get(
        'href')
    for item in items:
        url += str(item)
    return url


def parse(group_number):
    url = ''
    html = get_html(URL)
    if html.status_code == 200:
        url = str(get_content(html.text, group_number))
    else:
        print("errore!")
    data = str(url).split('/', maxsplit=4)
    return URL + data[4]
