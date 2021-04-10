#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import telebot
from bs4 import BeautifulSoup

import Config
from Schedule_parse import Group_parser


days = []
time_subject_info = []
day_lessons = []

#    day.append({
#        'Day': item.find('div', class_='schedule__date').get_text(strip=True),
#       'Time': item.find('div', class_='lesson__subject').get_text(strip=True)
#   })

#URL = str(Group_parser.parse("3530902/90002", "661902517"))
bot = telebot.TeleBot(Config.TOKEN, threaded=False)
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.100 Safari/537.36',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    content = ''
    soup = BeautifulSoup(html, 'html.parser')
    if not soup.find('li', class_='schedule__empty'):
        items = soup.find_all('li', class_='schedule__day')
        for item in items:
            days.append(
                item.find('div', 'schedule__date').get_text(strip=True)
            )
            lessons = item.find_all('li', class_='lesson')
            day_lessons.append(len(lessons))
            for lesson in lessons:
                # teacher = ''
                time_subject = lesson.find('div', class_='lesson__subject').get_text()
                info = lesson.find('div', class_='lesson__type').get_text()
                # teacher = ''.join(item.find('div', class_='lesson__teachers', text=True))
                place = lesson.find('div', class_='lesson__places').get_text()
                time_subject_info.append(
                    time_subject + "," + info + "," + place
                    # 'Time,Subject': time_subject,
                    # 'info': info,
                    # 'teacher': teacher,
                    # 'place': place
                )
    else:
        print("schedules none")
        # print (''.join(item.findAll(text=True)))
        # days.append({
    #        'Day': {item.find_all('div', class_='schedule__date'), item.find_all('div', 'lesson__subject')}
    # Teacher.parse(lesson.find('div', class_='lesson__teachers').find_next('a').get('href'))
    # })
    return content


def parse(group_num, institute, id):
    content = ''
    URL = str(Group_parser.parse(str(group_num), str(institute)))
    if URL == 'None':
        bot.send_message(id, "Неправильный номер группы")
    else:
        i = 0
        day = 0
        html = get_html(URL)
        if html.status_code == 200:
            content = str(get_content(html.text))
        else:
            print("errore!")
        for num in day_lessons:
            content += str(days[day])
            content += "\n"
            while num > 0:
                temporary = str(time_subject_info[i]).split(',', maxsplit=2)
                for temp in temporary:
                    content += str(temp) + "\n"
                i += 1
                num -= 1
                content += "\n"
            day += 1
            content += "\n"
        bot.send_message(id, content)
