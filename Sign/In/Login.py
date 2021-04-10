#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import telebot
from telebot import types

import Config
import Sign.CheckData
import Menu.Menu

bot = telebot.TeleBot(Config.TOKEN, threaded=False)
connection = pymysql.connect(host="localhost",
                             user="root",
                             password="1234",
                             db="student")


def login(message):
    message_id = message.chat.id
    data = str(message.text).split('/', maxsplit=1)
    if Sign.CheckData.check(data):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT username, password FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            if table is None:
                bot.send_message(message_id, "Аккаунт не существует!")
            else:
                for username, password in table:
                    if username == data[0] and password == data[1]:
                        bot.send_message(message_id, "Вы успешно вошли!", reply_markup=types.ReplyKeyboardRemove())
                        bot.send_message(message_id, "Добро пожаловать!", reply_markup=Menu.Menu.student_menu())
                    else:
                        bot.send_message(message_id, "У вас уже есть аккаунт! Забыли логин или пароль?",
                                         reply_markup=Menu.Menu.forgot_password())
    else:
        bot.send_message(message_id, "Неккоректный ввод!")
