#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import telebot

import Config
from Profile import Group
from Menu import Menu
import Sign.Up.Register
import Sign.In.Login
from Schedule_parse import Schedule_parser

bot = telebot.TeleBot(Config.TOKEN, threaded=False)
connection = pymysql.connect(host="localhost",
                             user="root",
                             password="1234",
                             db="student")


@bot.callback_query_handler(func=lambda call: True)  # Обработка всех Inline меню
def forgot_log_pas(call):
    message_id = call.message.chat.id
    if call.data == 'forgot':  # Восстановление лог и пас
        with connection.cursor() as cursor:
            bot.delete_message(
                chat_id=message_id, message_id=call.message.message_id
            )
            cursor.execute("""SELECT username, password FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for username, password in table:
                bot.send_message(message_id, "login: %s\npassword: %s" % (
                    username, password))
    elif call.data == 'profile':  # Меню профиля
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.profile_menu())
    elif call.data == 'edit_profile':  # Редактирование профиля
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_profile())
    elif call.data == 'edit_institute':  # Редактировать институт
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
    elif call.data == 'ICaIP':  # Институты 1 Институт кибербезопасности и защиты информации
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" +
                           str("Институт кибербезопасности и защиты информации") + """' WHERE id = """ + str(
                message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'HI':  # Институты 2 Гуманитарный институт
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Гуманитарный институт") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'IBSaB':  # Институты 3 Институт биомедицинских систем и биотехнологий
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Институт биомедицинских систем и биотехнологий") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'IAMaM':  # Институты 4 Институт прикладной математики и механики
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Институт прикладной математики и механики") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'IMEMaT':  # Институты 5 Институт машиностроения, материалов и транспорта
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Институт машиностроения, материалов и транспорта") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'IPNaT':  # Институты 6 Институт физики, нанотехнологий и телекоммуникаций
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Институт физики, нанотехнологий и телекоммуникаций") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'ICSaT':  # Институты 7 Институт компьютерных наук и технологий
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Институт компьютерных наук и технологий") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'CEI':  # Институты 8 Инженерно-строительный институт
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Инженерно-строительный институт") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'IE':  # Институты 9 Институт энергетики
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Институт энергетики") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'IIMEaT':  # Институты 10 Институт промышленного менеджмента, экономики и торговли
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET institute = '""" + str(
                "Институт промышленного менеджмента, экономики и торговли") + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_institute())
            connection.commit()
    elif call.data == 'edit_course':  # Редактировать курс
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_course())
    elif call.data == "one":  # Курсы(номера)
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET course = '""" + str(
                1) + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_course())
            connection.commit()
    elif call.data == "two":
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET course = '""" + str(
                2) + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_course())
            connection.commit()
    elif call.data == "three":
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET course = '""" + str(
                3) + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_course())
            connection.commit()
    elif call.data == "four":
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE student.profile SET course = '""" + str(
                4) + """' WHERE id = """ + str(message_id))
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_course())
            connection.commit()
    elif call.data == 'edit_group_number':  # Редактировать номер группы
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        send = bot.send_message(message_id, "Введите номер группы, писать точный номер группы(для нормального "
                                            "функционирования бота\nНапример 3530902/90002")
        bot.register_next_step_handler(send, Group.write_group)
    # elif call.data == 'edit_language':  # Редактировать язык
    elif call.data == 'back_profile_menu':
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT lang, institute, course, group_number FROM student.profile WHERE id = """ + str(message_id))
            table = cursor.fetchall()
            for lang, institute, course, group_number in table:
                bot.send_message(message_id, "Ваш профиль:\nlanguage: %s\ninstitute: "
                                             "%s\ncourse: %s\ngroup: %s" % (
                                     lang, institute, course, group_number), reply_markup=Menu.edit_profile())
    elif call.data == 'campus_location':  # Меню кампуса(выбор(учебный корпус, общежитие))
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        bot.send_message(message_id, "Выберите:", reply_markup=Menu.campus())
    elif call.data == 'learning_campus':  # Меню учебного корпуса
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        bot.send_message(message_id, "Выберите:", reply_markup=Menu.learning_campus_location())
    elif call.data == 'Main_educational_building':  # Локации
        bot.send_location(message_id, 60.007284, 30.372888)
    elif call.data == 'Chemical_building_SPBPU':
        bot.send_location(message_id, 60.006636, 30.376370)
    elif call.data == 'Mechanical_body':
        bot.send_location(message_id, 60.008116, 30.376798)
    elif call.data == 'Hydrocasing_1':
        bot.send_location(message_id, 60.005823, 30.381838)
    elif call.data == 'Hydrocasing_2':
        bot.send_location(message_id, 60.006670, 30.383658)
    elif call.data == 'Hydrotower':
        bot.send_location(message_id, 60.005706, 30.374190)
    elif call.data == 'Laboratory_building':
        bot.send_location(message_id, 60.007241, 30.379728)
    elif call.data == 'REC_RAS':
        bot.send_location(message_id, 60.002331, 30.373653)
    elif call.data == 'educational_building_1':
        bot.send_location(message_id, 60.008830, 30.372904)
    elif call.data == 'educational_building_2':
        bot.send_location(message_id, 60.008543, 30.374732)
    elif call.data == 'educational_building_3':
        bot.send_location(message_id, 60.007178, 30.381806)
    elif call.data == 'educational_building_4':
        bot.send_location(message_id, 60.007215, 30.376780)
    elif call.data == 'educational_building_5':
        bot.send_location(message_id, 59.999731, 30.374464)
    elif call.data == 'educational_building_6':
        bot.send_location(message_id, 60.000158, 30.367635)
    elif call.data == 'educational_building_9':
        bot.send_location(message_id, 60.000819, 30.366429)
    elif call.data == 'educational_building_10':
        bot.send_location(message_id, 60.000513, 30.369484)
    elif call.data == 'educational_building_11':
        bot.send_location(message_id, 60.009128, 30.377989)
    elif call.data == 'educational_building_15':
        bot.send_location(message_id, 60.007579, 30.390807)
    elif call.data == 'Career_Guidance_Center':
        bot.send_location(message_id, 60.009448, 30.371751)
    elif call.data == 'educational_building_16':
        bot.send_location(message_id, 60.007898, 30.389548)
    elif call.data == '1st_professorial_building':
        bot.send_location(message_id, 60.005058, 30.369480)
    elif call.data == '2st_professorial_building':
        bot.send_location(message_id, 60.004922, 30.378148)
    elif call.data == 'House_of_Scientists_in_Lesnoy':
        bot.send_location(message_id, 60.004369, 30.379631)
    elif call.data == 'Sports_complex_Polytechnic':
        bot.send_location(message_id, 60.002615, 30.369074)
    elif call.data == 'IofIMEaT':
        bot.send_location(message_id, 59.994881, 30.358111)
    elif call.data == 'Research_building':
        bot.send_location(message_id, 60.006645, 30.379694)
    elif call.data == 'dorms':  # Общежития
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        bot.send_message(message_id, "Выберите:", reply_markup=Menu.dorms())
    elif call.data == 'dorms1':
        bot.send_location(message_id, 59.986288, 30.342155)
    elif call.data == 'dorms3':
        bot.send_location(message_id, 59.986589, 30.343271)
    elif call.data == 'dorms4':
        bot.send_location(message_id, 59.986637, 30.345546)
    elif call.data == 'dorms5':
        bot.send_location(message_id, 59.986155, 30.346546)
    elif call.data == 'dorms6':
        bot.send_location(message_id, 59.986563, 30.348069)
    elif call.data == 'dorms7':
        bot.send_location(message_id, 59.986637, 30.342874)
    elif call.data == 'dorms8':
        bot.send_location(message_id, 59.999295, 30.371917)
    elif call.data == 'dorms10':
        bot.send_location(message_id, 59.998490, 30.370509)
    elif call.data == 'dorms11':
        bot.send_location(message_id, 59.985559, 30.344411)
    elif call.data == 'dorms12':
        bot.send_location(message_id, 59.998801, 30.376077)
    elif call.data == 'dorms13':
        bot.send_location(message_id, 60.008579, 30.391760)
    elif call.data == 'dorms14':
        bot.send_location(message_id, 59.999611, 30.374935)
    elif call.data == 'dorms15':
        bot.send_location(message_id, 60.007367, 30.389563)
    elif call.data == 'dorms16':
        bot.send_location(message_id, 60.047808, 30.333892)
    elif call.data == 'dorms17':
        bot.send_location(message_id, 60.021653, 30.388381)
    elif call.data == 'dorms18':
        bot.send_location(message_id, 60.021920, 30.387360)
    elif call.data == 'dorms19':
        bot.send_location(message_id, 59.859016, 30.326972)
    elif call.data == 'dorms20':
        bot.send_location(message_id, 59.911528, 30.319771)
    elif call.data == 'inst':  # Гео институтов
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        bot.send_message(message_id, "Выберите:", reply_markup=Menu.institutes_location())
    elif call.data == 'hum':
        bot.send_message(message_id, "📞 +7(812)297-03-18\n✉ office@lingua.spbstu.ru\n📍 Санкт-Петербург, "
                                     "ул. Политехническая, д. 19, (ст.м. Площадь Мужества)")
        bot.send_location(message_id, 60.000128, 30.367555)
    elif call.data == 'ice':
        bot.send_message(message_id, "📞 +7(812)5352509\n✉ office.ice@spbstu.ru\n📍 Санкт-Петербург, Политехническая "
                                     "ул., 29 Гидрокорпус-1, СПбПУ. Очное отделение: ауд. 220")
        bot.send_location(message_id, 60.005780, 30.381920)
    elif call.data == 'ibmst':
        bot.send_message(message_id, "📞 +7(812)290-95-00\n✉ vlasova.ol@spbstu.ru\n📍 Россия, Санкт-Петербург, Хлопина "
                                     "д.11, ауд.201")
        bot.send_location(message_id, 59.999631, 30.374781)
    elif call.data == 'caip':
        bot.send_message(message_id, "📞 +7(812)5527632\n✉ dmitry@ssl.stu.neva.ru\n📍 ул. Политехническая. 29, ГУК, "
                                     "каб. 173")
        bot.send_location(message_id, 60.007486, 30.373069)
    elif call.data == 'icst':
        bot.send_message(message_id, "📞 +7(911)8424506\n✉ office@icc.spbstu.ru\n📍 ул.Политехническая, дом 29В, "
                                     "Санкт-Петербург, 306 ауд.")
        bot.send_location(message_id, 60.007254, 30.381628)
    elif call.data == 'immit':
        bot.send_message(message_id, "📞 +7(812)5526623\n✉ karantin_immit@spbstu.ru\n📍 Санкт-Петербург, "
                                     "ул. Политехническая, дом 29, 1-й уч. корпус, ауд. 409")
        bot.send_location(message_id, 60.008829, 30.372928)
    elif call.data == 'iamt':
        bot.send_message(message_id, "📞 +7(812)5916528\n✉ iamt@spbstu.ru\n📍 г. Санкт-Петербург, ул. Политехническая "
                                     "д. 29АФ, Научно-исследовательский, Г.3.10"
                                     "корпус СПбПУ")
        bot.send_location(message_id, 60.006650, 30.379573)
    elif call.data == 'iamm':
        bot.send_message(message_id, "📞 +7(812)5526508\n✉ office@iamm.spbstu.ru\n📍 ул. Политехническая, дом 29, "
                                     "2-й уч. к., пом. 336, 338, Санкт-Петербург")
        bot.send_location(message_id, 60.008541, 30.374693)
    elif call.data == 'phnt':
        bot.send_message(message_id, "📞 +7(812)5529516\n✉ office@phnt.spbstu.ru\n📍 Ул. Политехническая 29, "
                                     "2 учебный корпус, четвертый этаж, аудитория 437")
        bot.send_location(message_id, 60.008541, 30.374693)
    elif call.data == 'ifkst':
        bot.send_message(message_id, "📞 +7(812)7750530 добавочный 3301\n✉ ifkst@spbstu.ru\n📍 Санкт-Петербург, "
                                     "улица Политехническая, 27")
        bot.send_location(message_id, 60.002771, 30.369011)
    elif call.data == 'iets':
        bot.send_message(message_id, "📞 +7(812)5527627 +7(812)5528945\n✉ office.ie@spbstu.ru\n📍 ул. Политехническая, "
                                     "д. 29, Главный учебный корпус, ауд. 262, Санкт-Петербург")
        bot.send_location(message_id, 60.007301, 30.372897)
    elif call.data == 'imet':
        bot.send_message(message_id, "📞 +79218450312\n✉ office@imet.spbstu.ru\n📍 Санкт-Петербург, Новороссийская "
                                     "ул., 50, каб. 1203")
        bot.send_location(message_id, 59.994798, 30.357886)
    elif call.data == 'iep':
        bot.send_message(message_id, "📞 +7(812)6066220\n📍 Гражданский проспект, 28, каб. 221")
        bot.send_location(message_id, 60.007302, 30.390336)
    elif call.data == 'back_campus':
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        bot.send_message(message_id, "Выберите:", reply_markup=Menu.campus())
    elif call.data == 'schedule':  # Расписание
        with connection.cursor() as cursor:
            cursor.execute("""SELECT institute FROM student.profile WHERE id = """ + str(message_id))
            student_institute = cursor.fetchone()
            cursor.execute("""SELECT group_number FROM student.profile WHERE id = """ + str(message_id))
            student_group_num = cursor.fetchone()
            if (student_institute is None) or (student_group_num is None):
                bot.send_message(message_id, "Заполните профиль!")
            else:
                group_num = ""
                institute = ""
                for group in student_group_num:
                    group_num = group
                for inst in student_institute:
                    institute = inst
                Schedule_parser.parse(group_num, institute, message_id)
    elif call.data == 'main_menu':  # Главное меню
        bot.delete_message(
            chat_id=message_id, message_id=call.message.message_id
        )
        bot.send_message(message_id, "Главное меню", reply_markup=Menu.student_menu())


@bot.message_handler(commands=['start'])  # Обработка команды start
def start_bot(message):
    message_id = message.chat.id
    bot.send_message(message_id, "Приветствую тебя, <b>{0.first_name}</b>!\nДавай познакомимся, я Пётр – твой "
                                 "персональный бот-помощник.\nДля начала, укажи, кем ты приходишься Политеху))\nЕсли "
                                 "хочешь узнать больше обо мне, нажми «Инфо».".format(message.from_user, bot.get_me(
    )), parse_mode='html', reply_markup=Menu.start_menu())


@bot.message_handler(content_types=['text'])
def text_message(message):
    message_id = message.chat.id
    if message.chat.type == 'private':
        with connection.cursor() as cursor:
            if message.text == 'Абитуриент':
                bot.send_message(message_id,
                                 "Хочешь поступить в Политех Петра?\nГотов протянуть руку помощи!\n<b>Почему стоит "
                                 "выбрать "
                                 "Политех?</b>\nСпбПУ входит в топ лучших высших учебных заведения России по данным "
                                 "федерально "
                                 "го портала российского образования.\nПо данным QS World University Rankings "
                                 "университет "
                                 "занимает 6 место по России.\nУниверситет включает в себя 12 институтов, филиалы в "
                                 "гор "
                                 "одах Чебоксары, Сосновый Бор и Череповец, научно-технологический институт, научно-обр"
                                 "азовательные центры, ряд специализированных научно-производственных "
                                 "структур.\nУниверс "
                                 "итетский городок расположен на северо-востоке города, включает 30 учебных и научно-п"
                                 "роизводственных корпусов, 13 общежитий, 10 жилых зданий, Дом Ученых и спортивный комп"
                                 "лекс.\nУниверситет сотрудничает более чем с 100 учреждениями по Европе (из них более "
                                 "30 в Германии), с 40 в Азии, с 7 в США и 8 в странах Африки.\nКомплекс спортивных соо"
                                 "ружений включает в себя: плавательный бассейн, баскетбольный и волейбольный залы, за"
                                 "лы борьбы и бокса, гимнастический зал, лыжная база, скалодром, зал тяжелой атлетики, "
                                 "шахматный клуб, стадион с двумя футбольными полями и хоккейной коробкой, теннисным "
                                 "кортом, гимнастическим городком и игровыми площадками.\nВсё необходимое для поступ"
                                 "ления ты можешь найти здесь:\nhttps://www.spbstu.ru/abit/bachelor/\nТак же лови кл"
                                 "ассные группы в ВК: \nhttps://vk.com/intellect_club\nhttps://vk.com/poly_studklub "
                                 "\nhttps"
                                 "://vk.com/fan_zenit_spbpu\nhttps://vk.com/so_politeh\nhttps://vk.com"
                                 "/internationalpoly"
                                 "tech\nhttps://vk.com/open.spbstu\nhttps://vk.com/politehpiter\nhttps://vk.com"
                                 "/polymeme "
                                 "\nhttps://vk.com/citatnik_spbstu", parse_mode='html',
                                 reply_markup=Menu.start_menu())
            if message.text == 'Студент':
                bot.send_message(message_id, "Регистрация, Вход", reply_markup=Menu.student_log())
            if message.text == 'Регистрация':
                send = bot.send_message(message_id, "Введите логин/пароль через '/', например sasha/1234")
                bot.register_next_step_handler(send, Sign.Up.Register.register)
            if message.text == 'Вход':
                send = bot.send_message(message_id, "Введите логин/пароль через '/', например sasha/1234")
                bot.register_next_step_handler(send, Sign.In.Login.login)


bot.polling(none_stop=True)
