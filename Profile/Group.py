import pymysql
import telebot

import Config
from Menu import Menu

bot = telebot.TeleBot(Config.TOKEN, threaded=False)
connection = pymysql.connect(host="localhost",
                             user="root",
                             password="1234",
                             db="student")


def write_group(message):
    message_id = message.chat.id
    with connection.cursor() as cursor:
        cursor.execute("""UPDATE student.profile SET group_number = '""" + str(
            message.text) + """' WHERE id = """ + str(message_id))
        connection.commit()
        cursor.execute(
            """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
        table = cursor.fetchall()
        for lang, institute, course, group_number in table:
            bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                         "%s\ncourse: %s\ngroup: %s" % (
                                 lang, institute, course, group_number), reply_markup=Menu.edit_profile())
