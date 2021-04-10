#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import telebot
from bs4 import BeautifulSoup

import Config
from Schedule_parse import Institute_parser, Error_parser

institute = ""


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.100 Safari/537.36',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html, group_number):
    url = ''
    soup = BeautifulSoup(html, 'html.parser')
    search = soup.findAll('a', class_='groups-list__link', text=str(group_number))
    if len(search) == 0:
        #bot.send_message(id, "Неправильный номер группы")
        return None
    else:
        items = soup.find('a', class_='groups-list__link', text=str(group_number)).get('href')
        for item in items:
            url += str(item)
        return url


def parse(group_number, institute):
    url = ''
    URL = str(Institute_parser.parse(institute) + "/")
    html = get_html(URL)
    if html.status_code == 200:
        url = str(get_content(html.text, str(group_number)))
    if url == 'None':
        return 'None'
    else:
        data = str(url).split('/', maxsplit=4)
        return URL + data[4]
