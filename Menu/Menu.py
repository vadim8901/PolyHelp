#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telebot import types


### Основное меню


def start_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    student = types.KeyboardButton("Студент")
    enrolle = types.KeyboardButton("Абитуриент")
    info = types.KeyboardButton("Инфо")
    markup.add(student, enrolle)
    markup.row(info)
    return markup


def student_log():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    register = types.KeyboardButton("Регистрация")
    login = types.KeyboardButton("Вход")
    markup.add(register, login)
    return markup


def forgot_password():
    markup = types.InlineKeyboardMarkup()
    forgot = types.InlineKeyboardButton(text="Да", callback_data="forgot")
    markup.add(forgot)
    return markup


def student_menu():
    markup = types.InlineKeyboardMarkup()
    profile = types.InlineKeyboardButton(text="Профиль", callback_data="profile")
    campus_location = types.InlineKeyboardButton(text="Карта кампуса", callback_data="campus_location")
    schedule = types.InlineKeyboardButton(text="Расписание", callback_data="schedule")
    markup.add(profile)
    markup.row(campus_location)
    markup.row(schedule)
    return markup


### Меню "Профиль"

def profile_menu():
    markup = types.InlineKeyboardMarkup()
    edit_profile = types.InlineKeyboardButton(text="Редактировать профиль", callback_data="edit_profile")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.add(edit_profile)
    markup.row(main_menu)
    return markup


def edit_profile():
    markup = types.InlineKeyboardMarkup()
    edit_institute = types.InlineKeyboardButton(text="Редактировать институт", callback_data="edit_institute")
    edit_course = types.InlineKeyboardButton(text="Редактировать курс", callback_data="edit_course")
    edit_group_number = types.InlineKeyboardButton(text="Редактировать номер группы", callback_data="edit_group_number")
    edit_language = types.InlineKeyboardButton(text="Изменить язык", callback_data="edit_language")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.add(edit_institute)
    markup.row(edit_course)
    markup.row(edit_group_number)
    markup.row(edit_language)
    markup.row(main_menu)
    return markup


def edit_institute():
    markup = types.InlineKeyboardMarkup()
    ICaIP = types.InlineKeyboardButton(text="Институт кибербезопасности и защиты информации", callback_data="ICaIP")
    HI = types.InlineKeyboardButton(text="Гуманитарный институт", callback_data="HI")
    IBSaB = types.InlineKeyboardButton(text="Институт биомедицинских систем и биотехнологий", callback_data="IBSaB")
    IAMaM = types.InlineKeyboardButton(text="Институт прикладной математики и механики", callback_data="IAMaM")
    IMEMaT = types.InlineKeyboardButton(text="Институт машиностроения, материалов и транспорта", callback_data="IMEMaT")
    IPNaT = types.InlineKeyboardButton(text="Институт физики, нанотехнологий и телекоммуникаций", callback_data="IPNaT")
    ICSaT = types.InlineKeyboardButton(text="Институт компьютерных наук и технологий", callback_data="ICSaT")
    CEI = types.InlineKeyboardButton(text="Инженерно-строительный институт", callback_data="CEI")
    IE = types.InlineKeyboardButton(text="Институт энергетики", callback_data="IE")
    IIMEaT = types.InlineKeyboardButton(text="Институт промышленного менеджмента, экономики и торговли",
                                        callback_data="IIMEaT")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.add(ICaIP)
    markup.row(HI)
    markup.row(IBSaB)
    markup.row(IAMaM)
    markup.row(IMEMaT)
    markup.row(IPNaT)
    markup.row(ICSaT)
    markup.row(CEI)
    markup.row(IE)
    markup.row(IIMEaT)
    markup.row(main_menu)
    return markup


def edit_course():
    markup = types.InlineKeyboardMarkup()
    course_one = types.InlineKeyboardButton(text="1", callback_data="one")
    course_two = types.InlineKeyboardButton(text="2", callback_data="two")
    course_three = types.InlineKeyboardButton(text="3", callback_data="three")
    course_four = types.InlineKeyboardButton(text="4", callback_data="four")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.add(course_one, course_two)
    markup.row(course_three, course_four)
    markup.row(main_menu)
    return markup


### Меню "Кампус"


def campus():
    markup = types.InlineKeyboardMarkup()
    learning_campus = types.InlineKeyboardButton(text="Учебные корпуса", callback_data="learning_campus")
    dorms = types.InlineKeyboardButton(text="Общежития", callback_data="dorms")
    institutes = types.InlineKeyboardButton(text="Институты", callback_data="inst")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.add(learning_campus)
    markup.row(dorms)
    markup.row(institutes)
    markup.row(main_menu)
    return markup


def learning_campus_location():
    markup = types.InlineKeyboardMarkup()
    Main_educational_building = types.InlineKeyboardButton(text="Главный учебный корпус",
                                                           callback_data="Main_educational_building")
    Chemical_building_SPBPU = types.InlineKeyboardButton(text="Химический корпус СПБПУ",
                                                         callback_data="Chemical_building_SPBPU")
    Mechanical_body = types.InlineKeyboardButton(text="Механический корпус", callback_data="Mechanical_body")
    Hydrocasing_1 = types.InlineKeyboardButton(text="Гидрокорпус-1", callback_data="Hydrocasing_1")
    Hydrocasing_2 = types.InlineKeyboardButton(text="Гидрокорпус-2", callback_data="Hydrocasing_2")
    Hydrotower = types.InlineKeyboardButton(text="Гидробашня", callback_data="Hydrotower")
    Laboratory_building = types.InlineKeyboardButton(text="Лабораторный корпус", callback_data="Laboratory_building")
    REC_RAS = types.InlineKeyboardButton(text="НОЦ РАН", callback_data="REC_RAS")
    educational_building_1 = types.InlineKeyboardButton(text="1-ый учебный корпус",
                                                        callback_data="educational_building_1")
    educational_building_2 = types.InlineKeyboardButton(text="2-ой учебный корпус",
                                                        callback_data="educational_building_2")
    educational_building_3 = types.InlineKeyboardButton(text="3-ий учебный корпус",
                                                        callback_data="educational_building_3")
    educational_building_4 = types.InlineKeyboardButton(text="4-ый учебный корпус",
                                                        callback_data="educational_building_4")
    educational_building_5 = types.InlineKeyboardButton(text="5-ый учебный корпус",
                                                        callback_data="educational_building_5")
    educational_building_6 = types.InlineKeyboardButton(text="6-ой учебный корпус",
                                                        callback_data="educational_building_6")
    educational_building_9 = types.InlineKeyboardButton(text="9-ый учебный корпус",
                                                        callback_data="educational_building_9")
    educational_building_10 = types.InlineKeyboardButton(text="10-ый учебный корпус",
                                                         callback_data="educational_building_10")
    educational_building_11 = types.InlineKeyboardButton(text="11-ый учебный корпус",
                                                         callback_data="educational_building_11")
    educational_building_15 = types.InlineKeyboardButton(text="15-ый учебный корпус",
                                                         callback_data="educational_building_15")
    Career_Guidance_Center = types.InlineKeyboardButton(
        text="Центр профориентации и довузовской подготовки СПбПУ Петра Великого",
        callback_data="Career_Guidance_Center")
    educational_building_16 = types.InlineKeyboardButton(text="16-ый учебный корпус",
                                                         callback_data="educational_building_16")
    professorial_building_1 = types.InlineKeyboardButton(text="1-й профессорский корпус",
                                                         callback_data="1st_professorial_building")
    professorial_building_2 = types.InlineKeyboardButton(text="2-й профессорский корпус",
                                                         callback_data="2st_professorial_building")
    House_of_Scientists_in_Lesnoy = types.InlineKeyboardButton(text="Дом ученых в Лесном",
                                                               callback_data="House_of_Scientists_in_Lesnoy")
    Sports_complex_Polytechnic = types.InlineKeyboardButton(text="Спортивный комплекс 'Политехник'",
                                                            callback_data="Sports_complex_Polytechnic")
    IofIMEaT = types.InlineKeyboardButton(text="Институт промышленного Менеджмента, Экономики и Торговли",
                                          callback_data="IofIMEaT")
    Research_building = types.InlineKeyboardButton(text="Научно-исследовательский корпус ",
                                                   callback_data="Research_building")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.add(Main_educational_building)
    markup.row(Chemical_building_SPBPU)
    markup.row(Mechanical_body)
    markup.row(Hydrocasing_1)
    markup.row(Hydrocasing_2)
    markup.row(Hydrotower)
    markup.row(Laboratory_building)
    markup.row(REC_RAS)
    markup.row(educational_building_1)
    markup.row(educational_building_2)
    markup.row(educational_building_3)
    markup.row(educational_building_4)
    markup.row(educational_building_5)
    markup.row(educational_building_6)
    markup.row(educational_building_9)
    markup.row(educational_building_10)
    markup.row(educational_building_11)
    markup.row(educational_building_15)
    markup.row(Career_Guidance_Center)
    markup.row(educational_building_16)
    markup.row(professorial_building_1)
    markup.row(professorial_building_2)
    markup.row(House_of_Scientists_in_Lesnoy)
    markup.row(Sports_complex_Polytechnic)
    markup.row(IofIMEaT)
    markup.row(Research_building)
    markup.row(main_menu)
    return markup


def dorms():
    markup = types.InlineKeyboardMarkup()
    dorms1 = types.InlineKeyboardButton(text="Общежитие №1", callback_data="dorms1")
    dorms3 = types.InlineKeyboardButton(text="Общежитие №3", callback_data="dorms3")
    dorms4 = types.InlineKeyboardButton(text="Общежитие №4", callback_data="dorms4")
    dorms5 = types.InlineKeyboardButton(text="Общежитие №5, 5б", callback_data="dorms5")
    dorms6 = types.InlineKeyboardButton(text="Общежитие №6м, 6ф", callback_data="dorms6")
    dorms7 = types.InlineKeyboardButton(text="Общежитие №7", callback_data="dorms7")
    dorms8 = types.InlineKeyboardButton(text="Общежитие №8", callback_data="dorms8")
    dorms10 = types.InlineKeyboardButton(text="Общежитие №10", callback_data="dorms10")
    dorms11 = types.InlineKeyboardButton(text="Общежитие №11", callback_data="dorms11")
    dorms12 = types.InlineKeyboardButton(text="Общежитие №12", callback_data="dorms12")
    dorms13 = types.InlineKeyboardButton(text="Общежитие №13", callback_data="dorms13")
    dorms14 = types.InlineKeyboardButton(text="Общежитие №14", callback_data="dorms14")
    dorms15 = types.InlineKeyboardButton(text="Общежитие №15", callback_data="dorms15")
    dorms16 = types.InlineKeyboardButton(text="Общежитие №16", callback_data="dorms16")
    dorms17 = types.InlineKeyboardButton(text="Общежитие №17", callback_data="dorms17")
    dorms18 = types.InlineKeyboardButton(text="Общежитие №18", callback_data="dorms18")
    dorms19 = types.InlineKeyboardButton(text="Общежитие №19", callback_data="dorms19")
    dorms20 = types.InlineKeyboardButton(text="Общежитие №20", callback_data="dorms20")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.row(dorms1, dorms3)
    markup.row(dorms4, dorms5)
    markup.row(dorms6, dorms7)
    markup.row(dorms8, dorms10)
    markup.row(dorms11, dorms12)
    markup.row(dorms13, dorms14)
    markup.row(dorms15, dorms16)
    markup.row(dorms17, dorms18)
    markup.row(dorms19, dorms20)
    markup.row(main_menu)
    return markup


def institutes_location():
    markup = types.InlineKeyboardMarkup()
    hum = types.InlineKeyboardButton(text="Гуманитарный институт", callback_data="hum")
    ice = types.InlineKeyboardButton(text="Инженерно-строительный институт", callback_data="ice")
    ibmst = types.InlineKeyboardButton(text="Институт биомедицинских систем и биотехнологий", callback_data="ibmst")
    caip = types.InlineKeyboardButton(text="Институт кибербезопасности и защиты информации", callback_data="caip")
    icst = types.InlineKeyboardButton(text="Институт компьютерных наук и технологий", callback_data="icst")
    immit = types.InlineKeyboardButton(text="Институт машиностроения, материалов и транспорта", callback_data="immit")
    iamt = types.InlineKeyboardButton(text="Институт передовых производственных технологий", callback_data="iamt")
    iamm = types.InlineKeyboardButton(text="Институт прикладной математики и механики", callback_data="iamm")
    phnt = types.InlineKeyboardButton(text="Институт физики, нанотехнологий и телекоммуникаций", callback_data="phnt")
    ifkst = types.InlineKeyboardButton(text="Институт физической культуры, спорта и туризма", callback_data="ifkst")
    iets = types.InlineKeyboardButton(text="Институт энергетики", callback_data="iets")
    imet = types.InlineKeyboardButton(text="Институт промышленного менеджмента, экономики и торговли", callback_data="imet")
    iep = types.InlineKeyboardButton(text="Высшая школа международных образовательных программ", callback_data="iep")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.row(hum)
    markup.row(ice)
    markup.row(ibmst)
    markup.row(caip)
    markup.row(icst)
    markup.row(immit)
    markup.row(iamt)
    markup.row(iamm)
    markup.row(phnt)
    markup.row(ifkst)
    markup.row(iets)
    markup.row(imet)
    markup.row(iep)
    markup.row(main_menu)
    return markup


### Расписание

def week():
    markup = types.InlineKeyboardMarkup()
    next_week = types.InlineKeyboardButton(text="Следующая неделя", callback_data="next_week")
    last_week = types.InlineKeyboardButton(text="Предыдущая неделя", callback_data="last_week")
    main_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    markup.row(next_week, last_week)
    markup.row(main_menu)
    return markup
