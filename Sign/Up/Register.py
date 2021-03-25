#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import telebot

import Config
import Sign.CheckData
from Menu import Menu

bot = telebot.TeleBot(Config.TOKEN, threaded=False)
connection = pymysql.connect(host="localhost",
                             user="root",
                             password="1234",
                             db="student")


def register(message):
    message_id = message.chat.id
    data = str(message.text).split('/', maxsplit=1)
    if Sign.CheckData.check(data):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT id FROM student.profile WHERE id = """ + str(message_id))
            id_user = cursor.fetchone()
            if id_user is None:
                cursor.execute(
                    """INSERT INTO student.profile (id) VALUE """ + """(""" + str(message_id) + """)""")
                cursor.execute("""UPDATE student.profile SET username = '""" + str(
                    data[0]) + """' WHERE id = """ + str(message_id))
                cursor.execute("""UPDATE student.profile SET password = '""" + str(
                    data[1]) + """' WHERE id = """ + str(message_id))
                connection.commit()
                bot.send_message(message_id, "Вы успешно зарегистрировались! нажмите вход, для продолжения")
            else:
                bot.send_message(message_id, "У вас уже есть аккаунт! Забыли логин или пароль?",
                                 reply_markup=Menu.forgot_password())
    else:
        bot.send_message(message_id, "Error! / не забывай. Повтори")
