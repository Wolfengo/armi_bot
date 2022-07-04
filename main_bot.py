import telebot
import requests
import time
import datetime
import settings
import bot_works
import buttons
from bot_bd import Armi_in_db
from parks_db import Parks_in_db
from telebot import types

Work_in_db = Armi_in_db(settings.folder())
Parks = Parks_in_db(settings.folder())
bot = telebot.TeleBot(settings.test())
Blocks = buttons.Buttons(settings.test())
Buttons = buttons
logger = telebot.logger

global id_tele
id_tele = []

global need_money_balance
need_money_balance = []


# def menu_districts():
#     keyboard = types.InlineKeyboardMarkup()
#     my_flit = types.InlineKeyboardButton(text="Майфлит", callback_data='my_flit')
#     drive = types.InlineKeyboardButton(text="Драйв", callback_data='drive')
#     park = types.InlineKeyboardButton(text="Выбрать парк из списка", callback_data='park')
#     back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
#     keyboard.add(my_flit)
#     keyboard.add(drive)
#     keyboard.add(park)
#     keyboard.add(back_rooms)
#     return keyboard


# def districts1():
#     keyboard = types.InlineKeyboardMarkup()
#     central = types.InlineKeyboardButton(text="Центральный район", callback_data='central')
#     soviet = types.InlineKeyboardButton(text="Советский район", callback_data='soviet')
#     pervomai = types.InlineKeyboardButton(text="Первомайский район", callback_data='pervomai')
#     up = types.InlineKeyboardButton(text="Вперёд", callback_data='up')
#     down = types.InlineKeyboardButton(text="Вернуться в меню", callback_data='down')
#     keyboard.add(central)
#     keyboard.add(soviet)
#     keyboard.add(pervomai)
#     keyboard.add(down, up)
#     return keyboard
#
#
# def districts2():
#     keyboard = types.InlineKeyboardMarkup()
#     partiz = types.InlineKeyboardButton(text="Партизанский район", callback_data='partiz')
#     zavod = types.InlineKeyboardButton(text="Заводской район", callback_data='zavod')
#     lenin = types.InlineKeyboardButton(text="Ленинский район", callback_data='lenin')
#     up = types.InlineKeyboardButton(text="Вперёд", callback_data='up')
#     down = types.InlineKeyboardButton(text="Назад", callback_data='down')
#     keyboard.add(partiz)
#     keyboard.add(zavod)
#     keyboard.add(lenin)
#     keyboard.add(down, up)
#     return keyboard
#
#
# def districts3():
#     keyboard = types.InlineKeyboardMarkup()
#     october = types.InlineKeyboardButton(text="Октябрьский район", callback_data='october')
#     moscow = types.InlineKeyboardButton(text="Московский район", callback_data='moscow')
#     frunze = types.InlineKeyboardButton(text="Фрунзенский район", callback_data='frunze')
#     up = types.InlineKeyboardButton(text="Вернуться в меню", callback_data='up')
#     down = types.InlineKeyboardButton(text="Назад", callback_data='down')
#     keyboard.add(october)
#     keyboard.add(moscow)
#     keyboard.add(frunze)
#     keyboard.add(down, up)
#     return keyboard


# def if_not_drive():
#     keyboard = types.InlineKeyboardMarkup()
#     reg_driver = types.InlineKeyboardButton(text="Войти водителем", callback_data='reg_driver')
#     reg_park = types.InlineKeyboardButton(text="Войти партнёром", callback_data="reg_park")
#     keyboard.add(reg_driver)
#     keyboard.add(reg_park)
#     return keyboard


def yes_no_new_car():
    keyboard = types.InlineKeyboardMarkup()
    yes_new_car = types.InlineKeyboardButton(text="Да", callback_data='yes_new_car')
    no_new_doc = types.InlineKeyboardButton(text="Нет", callback_data="no_new_doc")
    keyboard.add(yes_new_car)
    keyboard.add(no_new_doc)
    return keyboard


def yes_no_admin_reg_doc():
    keyboard = types.InlineKeyboardMarkup()
    yes_reg_admin_docks = types.InlineKeyboardButton(text="Да", callback_data='yes_reg_admin_docks')
    back_menu = types.InlineKeyboardButton(text="Нет", callback_data="back_menu")
    keyboard.add(yes_reg_admin_docks)
    keyboard.add(back_menu)
    return keyboard


def yes_no_admin_reg_cash():
    keyboard = types.InlineKeyboardMarkup()
    yes_reg_admin_cash = types.InlineKeyboardButton(text="Да", callback_data='yes_reg_admin_cash')
    back_menu = types.InlineKeyboardButton(text="Нет", callback_data="back_menu")
    keyboard.add(yes_reg_admin_cash)
    keyboard.add(back_menu)
    return keyboard


def yes_no_admin_reg_contact():
    keyboard = types.InlineKeyboardMarkup()
    yes_reg_admin_contact = types.InlineKeyboardButton(text="Да", callback_data='yes_reg_admin_contact')
    back_menu = types.InlineKeyboardButton(text="Нет", callback_data="back_menu")
    keyboard.add(yes_reg_admin_contact)
    keyboard.add(back_menu)
    return keyboard


def yes_no_new_boc():
    keyboard = types.InlineKeyboardMarkup()
    yes_new_doc = types.InlineKeyboardButton(text="Да", callback_data='yes_new_doc')
    no_new_doc = types.InlineKeyboardButton(text="Нет", callback_data="no_new_doc")
    keyboard.add(yes_new_doc)
    keyboard.add(no_new_doc)
    return keyboard


def room_for_driver():
    keyboard = types.InlineKeyboardMarkup()
    new_num_driver = types.InlineKeyboardButton(text="Поменять номер телефона", callback_data='new_num_driver')
    new_car_driver = types.InlineKeyboardButton(text="Заявка на смену машины", callback_data="new_car_driver")
    new_doc_driver = types.InlineKeyboardButton(text="Заявка на смену В/У", callback_data="new_doc_driver")
    money_ty_balance = types.InlineKeyboardButton(text="Перевод денег с безнала на баланс",
                                                  callback_data="money_ty_balance")
    my_info = types.InlineKeyboardButton(text="Моя информация", callback_data="my_info")
    keyboard.add(new_num_driver)
    keyboard.add(new_car_driver)
    keyboard.add(new_doc_driver)
    keyboard.add(money_ty_balance)
    keyboard.add(my_info)
    return keyboard


def room_for_driver_reg2():
    keyboard = types.InlineKeyboardMarkup()
    new_car_driver = types.InlineKeyboardButton(text="Заявка на смену машины", callback_data="new_car_driver")
    keyboard.add(new_car_driver)
    return keyboard


def room_for_driver_reg3():
    keyboard = types.InlineKeyboardMarkup()
    new_doc_driver = types.InlineKeyboardButton(text="Заявка на смену В/У", callback_data="new_doc_driver")
    keyboard.add(new_doc_driver)
    return keyboard


def admin_button():
    keyboard = types.InlineKeyboardMarkup()
    new_admin = types.InlineKeyboardButton(text="Добавить администратора", callback_data='new_admin')
    exists_admin = types.InlineKeyboardButton(text="Стать администратором", callback_data='exists_admin')
    new_num_admin = types.InlineKeyboardButton(text="Изменить номер телефона", callback_data='new_num_admin')
    not_drive = types.InlineKeyboardButton(text="Список не рассмотренных регистраций", callback_data='not_drive')
    not_money = types.InlineKeyboardButton(text="Запросы перевода безнала на баланс", callback_data='not_money')
    new_reg_num_driver = types.InlineKeyboardButton(text="Запросы на смену номера телефона",
                                                    callback_data='new_reg_num_driver')
    # all_info = types.InlineKeyboardButton(text="Общая сводка", callback_data='all_info')
    keyboard.add(new_admin)
    keyboard.add(exists_admin)
    keyboard.add(new_num_admin)
    keyboard.add(not_drive)
    keyboard.add(not_money)
    keyboard.add(new_reg_num_driver)
    # keyboard.add(all_info)
    return keyboard


def admin_reg():
    keyboard = types.InlineKeyboardMarkup()
    admin_reg_for_docks = types.InlineKeyboardButton(text="Администратор запросов", callback_data='admin_reg_for_docks')
    admin_reg_for_cash = types.InlineKeyboardButton(text="Администратор безнала", callback_data='admin_reg_for_cash')
    admin_reg_for_contact = types.InlineKeyboardButton(text="Администратор контактов",
                                                       callback_data='admin_reg_for_contact')
    back_menu = types.InlineKeyboardButton(text="Отмена", callback_data="back_menu")
    keyboard.add(admin_reg_for_docks)
    keyboard.add(admin_reg_for_cash)
    keyboard.add(admin_reg_for_contact)
    keyboard.add(back_menu)
    return keyboard


def admin_money_balance():
    keyboard = types.InlineKeyboardMarkup()
    add_money_balance = types.InlineKeyboardButton(text="Подтвердить", callback_data='add_money_balance')
    backup_money_balance = types.InlineKeyboardButton(text="Отказать", callback_data='backup_money_balance')
    later_money_balance = types.InlineKeyboardButton(text="Посмотрю позже", callback_data='later_money_balance')
    keyboard.add(add_money_balance)
    keyboard.add(backup_money_balance)
    keyboard.add(later_money_balance)
    return keyboard


def admin_reg_driver():
    keyboard = types.InlineKeyboardMarkup()
    add_driver = types.InlineKeyboardButton(text="Готово", callback_data='add_driver')
    backup_driver = types.InlineKeyboardButton(text="Отмена", callback_data='backup_driver')
    later_driver = types.InlineKeyboardButton(text="Посмотрю позже", callback_data='later_driver')
    keyboard.add(add_driver)
    keyboard.add(backup_driver)
    keyboard.add(later_driver)
    return keyboard


def admin_change_car_doc():
    keyboard = types.InlineKeyboardMarkup()
    add_car_doc = types.InlineKeyboardButton(text="Готово", callback_data='add_car_doc')
    backup_car_doc = types.InlineKeyboardButton(text="Отмена", callback_data='backup_car_doc')
    later_car_doc = types.InlineKeyboardButton(text="Посмотрю позже", callback_data='later_car_doc')
    keyboard.add(add_car_doc)
    keyboard.add(backup_car_doc)
    keyboard.add(later_car_doc)
    return keyboard


def admin_change_driver_doc():
    keyboard = types.InlineKeyboardMarkup()
    add_driver_doc = types.InlineKeyboardButton(text="Готово", callback_data='add_driver_doc')
    backup_driver_doc = types.InlineKeyboardButton(text="Отмена", callback_data='backup_driver_doc')
    later_driver_doc = types.InlineKeyboardButton(text="Посмотрю позже", callback_data='later_driver_doc')
    keyboard.add(add_driver_doc)
    keyboard.add(backup_driver_doc)
    keyboard.add(later_driver_doc)
    return keyboard


def admin_change_num_driver_phone():
    keyboard = types.InlineKeyboardMarkup()
    add_new_num = types.InlineKeyboardButton(text="Готово", callback_data='add_new_num')
    backup_new_num = types.InlineKeyboardButton(text="Отмена", callback_data='backup_new_num')
    later_driver_num = types.InlineKeyboardButton(text="Посмотрю позже", callback_data='later_driver_num')
    keyboard.add(add_new_num)
    keyboard.add(backup_new_num)
    keyboard.add(later_driver_num)
    return keyboard


def next_reg_driver():
    keyboard = types.InlineKeyboardMarkup()
    not_drive = types.InlineKeyboardButton(text="Продолжить", callback_data='not_drive')
    backup_driver = types.InlineKeyboardButton(text="Вернуться в меню", callback_data='back_menu')
    keyboard.add(not_drive)
    keyboard.add(backup_driver)
    return keyboard


def next_need_money():
    keyboard = types.InlineKeyboardMarkup()
    not_money = types.InlineKeyboardButton(text="Продолжить", callback_data='not_money')
    backup_driver = types.InlineKeyboardButton(text="Вернуться в меню", callback_data='back_menu')
    keyboard.add(not_money)
    keyboard.add(backup_driver)
    return keyboard


def who_i_have():
    pass


@bot.message_handler(commands=['start'])
def start(message):
    bot.clear_step_handler(message)
    # if not Work_in_db.user_exists(message.from_user.id):
    #     '''eсть ли юзер в базе, если нету, то создаём (сохраняет и id юзера и его имя аккаунта(если есть)'''
    #     Work_in_db.add_user(message.from_user.id, message.from_user.username)
    # if Work_in_db.exist_number_phone(message.from_user.id)[0][0] is None:
    #     pass
    # elif Work_in_db.exist_number_phone(message.from_user.id)[0][0] is not None:
    #     url = requests.get(f'{settings.URL}{Work_in_db.exist_number_phone(message.from_user.id)[0][0]}')
    #     if url.json()['status'] == 'EXISTS':
    #         pass
    #     elif url.json()['status'] == 'NOT_EXISTS':
    #         pass
    #     elif url.json()['status'] == 'BLOCKED':
    #         Work_in_db.add_user_register(message.from_user.id, '404')
    # if Work_in_db.user_exists_register(message.from_user.id)[0][0] == "404":
    #     bot.send_message(
    #         message.chat.id,
    #         f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
    #         f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
    # else:
    #     if not Work_in_db.user_exists_name(message.from_user.username):
    #         '''проверяем не сменил ли юзер имя аккаунта телеги, если да, то меняем'''
    #         Work_in_db.change_user_name(message.from_user.username, message.from_user.id)
    #     if str(Work_in_db.user_exists_register(message.from_user.id)[0][0]) == "0" or \
    #             str(Work_in_db.user_exists_register(message.from_user.id)[0][0]) == "2" or \
    #             str(Work_in_db.user_exists_register(message.from_user.id)[0][0]) == "3":
    #         welcome_driver(message)
    #     elif Work_in_db.user_exists_register(message.from_user.id)[0][0] is None:
    #         # if Work_in_db.exist_number_phone(message.from_user.id)[0][0] is None:
    #         #     mes = bot.send_message(
    #         #         message.chat.id,
    #         #         "Добро пожаловать в бот для водителя Armi!\n"
    #         #         "Вижу вы тут впервый раз! Напишите, пожалуйста, ваш рабочий номер телефона\n"
    #         #         "Пример: 375 29 1234567")
    #         #     bot.register_next_step_handler(mes, enter_chat_number)
    #         # else:
    #         if Work_in_db.user_exists_register(message.from_user.id)[0][0] is None:
    bot.send_message(
        message.chat.id,
        "Выберите нужный кабинет Armi\n",
        reply_markup=Buttons.if_not_drive())
    # elif Work_in_db.user_exists_register(message.from_user.id)[0][0] == "0":
    #     driver_register(message)


def driver_register(message):
    if Work_in_db.user_exists_auto(message.from_user.id)[0][0] is not None and \
            Work_in_db.user_exists_drive1(message.from_user.id)[0][0] is not None and \
            Work_in_db.user_exists_drive2(message.from_user.id)[0][0] is not None:
        bot.send_message(
            message.chat.id,
            f"Все документы уже были получены!\n"
            f"Я вас уведомлю после успешной регистрации и дам доступ к работе над "
            f"документами\n"
            f"По всем вопросам можете обратиться по номеру +{Work_in_db.take_first_admin_num()}\n"
            f"Или по ссылке: @{Work_in_db.take_first_admin_name()}")
    else:
        bot.send_message(
            message.chat.id,
            "Добро пожаловать в бот для водителя Armi!\n")
        bot.send_message(
            message.chat.id,
            "Выберите нужный кабинет Armi\n"
            "(Если вы ввели не верный номер телефона, после нажатия на кнопку, напишите 0)",
            reply_markup=Buttons.if_not_drive())


def enter_new_admin_number(message):
    phone = message.text
    number = []
    for num in phone:
        if num.isdigit() is True:
            number.append(num)
    if len(number) != 12:
        bot.send_message(
            message.chat.id,
            "Ошибка в номере телефона! Попробуйте ещё раз")
        number.clear()
        bot.register_next_step_handler(message, enter_new_admin_number)
    if len(number) != 0:
        full_number = '+'
        for i in number:
            full_number += i
        Work_in_db.add_admin_phone(message.from_user.id, full_number)
        bot.send_message(
            message.chat.id,
            "Номер телефона записан!\n")
        bot.send_message(
            message.chat.id,
            "Меню дополнительных настроек",
            reply_markup=admin_button())


def enter_chat_number(message):
    bot.delete_message(message.from_user.id, message.message_id - 1)
    keyboard = types.InlineKeyboardMarkup()
    back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
    keyboard.add(back_rooms)
    phone = message.text
    number = []
    for num in phone:
        if num.isdigit() is True:
            number.append(num)
    if len(number) != 12:
        bot.send_message(
            message.chat.id,
            "Ошибка в номере телефона! Попробуйте ещё раз",
            reply_markup=keyboard)
        number.clear()
        bot.register_next_step_handler(message, enter_chat_number)
    if len(number) != 0:
        full_number = ''
        for i in number:
            full_number += i
        try:
            Work_in_db.add_number_phone(message.from_user.id, full_number)
            url = requests.get(f'{settings.URL}{full_number}')
            if url.json()["status"] == "EXISTS":
                keyboard = types.InlineKeyboardMarkup()
                my_flit = types.InlineKeyboardButton(text="Майфлит", callback_data='my_flit')
                drive = types.InlineKeyboardButton(text="Драйв", callback_data='drive')
                park = types.InlineKeyboardButton(text="Выбрать парк из списка", callback_data='park')
                null_num_driver = types.InlineKeyboardButton(text="Введён не тот номер телефона",
                                                             callback_data='null_num_driver')
                back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
                keyboard.add(my_flit)
                keyboard.add(drive)
                keyboard.add(park)
                keyboard.add(null_num_driver)
                keyboard.add(back_rooms)
                Work_in_db.add_car_doc(message.from_user.id, 'in url data base')
                Work_in_db.add_drive_doc1(message.from_user.id, 'in url data base')
                Work_in_db.add_drive_doc2(message.from_user.id, 'in url data base')
                Work_in_db.add_num_car(message.from_user.id, url.json()['car']['regNumber'])
                Work_in_db.add_name_car(message.from_user.id, url.json()['car']['automaker'])
                Work_in_db.add_model_car(message.from_user.id, url.json()['car']['model'])
                Work_in_db.add_user_register(message.from_user.id, '0')
                """добавить имя, модель и номер машины в базу"""
                bot.send_message(
                    message.chat.id,
                    f"Номер телефона записан!\n"
                    f"Вижу вас в системе!\n"
                    f"Ваш номер телефона: +{Work_in_db.exist_number_phone(message.from_user.id)[0][0]}\n"
                    f"Ваша машина: {Work_in_db.take_name_car(message.from_user.id)[0][0]} "
                    f"{Work_in_db.take_model_car(message.from_user.id)[0][0]}, номер машины: "
                    f"{Work_in_db.take_num_car(message.from_user.id)[0][0]}\n"
                    f" \n"
                    f"У вас отсутствует подключение к парку.\n"
                    f'Мы можем предложить вам тарифы "Майфлит"(ИП) и "Драйв"(физ)\n'
                    f' \n'
                    f'Либо "Смартдрайв" - парк на выбор, '
                    f'при подключении к парку комиссия арми 0%:\n',
                    reply_markup=keyboard)
            elif url.json()["status"] == "NOT_EXISTS":
                if Work_in_db.user_exists_auto(message.from_user.id)[0][0] is None or \
                        Work_in_db.user_exists_drive1(message.from_user.id)[0][0] is None or \
                        Work_in_db.user_exists_drive2(message.from_user.id)[0][0] is None:
                    bot.send_message(
                        message.chat.id,
                        "Номер телефона записан!\n"
                        "Данные о регистрации в Armi отсутствуют!")
                    take_photo(message)
            elif url.json()["status"] == "BLOCKED":
                Work_in_db.add_user_register(message.from_user.id, '404')
                bot.send_message(
                    message.chat.id,
                    f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                    f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        except:
            bot.send_message(message.chat.id, f'Данный номер не может быть использован!\n'
                                              f'Обратитесь к администратору '
                                              f'@{Work_in_db.take_first_admin_name()[0][0]}\n'
                                              f'Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}')
            start(message)


def new_start_not_drive(message):
    if Work_in_db.user_exists_auto(message.from_user.id)[0][0] is None:
        bot.send_message(
            message.chat.id,
            "Данные о регистрации в Armi отсутствуют!")
        bot.send_message(
            message.chat.id,
            "Выберите как вы хотите сотрудничать с Armi\n"
            "(Если вы ввели не верный номер телефона, после нажатия на кнопку, напишите 0)",
            reply_markup=Buttons.if_not_drive())


def welcome_driver(message):
    if settings.TEST is True:
        bot.send_message(message.from_user.id, 'У вас отсутствует подключение к парку.\n'
                                               'Мы можем предложить вам тарифы "Майфлит"(ИП) и "Драйв"(физ)\n '
                                               ' \n'
                                               'Либо "Смартдрайв" - парк на выбор, '
                                               'при подключении к парку комиссия арми 0%:\n',
                         reply_markup=Buttons.menu_districts())

    else:
        if Work_in_db.take_name_driver(message.from_user.id)[0][0] is None:
            if Work_in_db.user_exists_register(message.from_user.id)[0][0] == '0':
                bot.send_message(
                    message.from_user.id,
                    f"Ваш номер телефона: +{Work_in_db.exist_number_phone(message.from_user.id)[0][0]}\n"
                    f"Ваша машина: {Work_in_db.take_name_car(message.from_user.id)[0][0]} "
                    f"{Work_in_db.take_model_car(message.from_user.id)[0][0]}, номер машины: "
                    f"{Work_in_db.take_num_car(message.from_user.id)[0][0]}",
                    reply_markup=room_for_driver())
            elif Work_in_db.user_exists_register(message.from_user.id)[0][0] == '2':
                if Work_in_db.user_exists_auto(message.from_user.id)[0][0] is None:
                    bot.send_message(
                        message.from_user.id,
                        f"Доброго времени суток!\n"
                        f"Пожалуйста, повторите отправку документа на авто! Ваша фотография была отклонена",
                        reply_markup=room_for_driver_reg2())
                else:
                    bot.send_message(
                        message.from_user.id,
                        f"Доброго времени суток!\n"
                        f"Ожидайте подтверждения регистрации, я вас уведомлю о результате регистрации", )
            elif Work_in_db.user_exists_register(message.from_user.id)[0][0] == '3':
                if Work_in_db.user_exists_drive1(message.from_user.id) is None or \
                        Work_in_db.user_exists_drive2(message.from_user.id) is None:
                    bot.send_message(
                        message.from_user.id,
                        f"Доброго времени суток!\n"
                        f"Пожалуйста, повторите отправку В/У! Ваши фотографии были отклонены",
                        reply_markup=room_for_driver_reg3())
                else:
                    bot.send_message(
                        message.from_user.id,
                        f"Доброго времени суток!\n"
                        f"Ожидайте подтверждения регистрации, я вас уведомлю о результате регистрации", )
        else:
            bot.send_message(
                message.chat.id,
                f"Доброго времени суток {Work_in_db.take_name_driver(message.from_user.id)[0][0]}!\n"
                f"Ваш номер телефона: +{Work_in_db.exist_number_phone(message.from_user.id)[0][0]}\n"
                f"Ваша машина: {Work_in_db.take_name_car(message.from_user.id)[0][0]} "
                f"{Work_in_db.take_model_car(message.from_user.id)[0][0]}, номер машины: "
                f"{Work_in_db.take_num_car(message.from_user.id)[0][0]}",
                reply_markup=room_for_driver())


def photo(message):
    try:
        if Work_in_db.user_exists_auto(message.from_user.id)[0][0] is None:
            '''записываем айди фото документа на авто'''
            bot.delete_message(message.from_user.id, message.message_id - 1)
            car_doc = message.photo[0].file_id
            Work_in_db.add_car_doc(message.chat.id, car_doc)
            take_photo(message)
        elif Work_in_db.user_exists_drive1(message.from_user.id)[0][0] is None:
            '''записываем айди фото лицевой стороны прав'''
            bot.delete_message(message.from_user.id, message.message_id - 1)
            driver_doc1 = message.photo[0].file_id
            Work_in_db.add_drive_doc1(message.chat.id, driver_doc1)
            take_photo(message)
        elif Work_in_db.user_exists_drive2(message.from_user.id)[0][0] is None:
            '''записываем айди фото обратной стороны прав'''
            bot.delete_message(message.from_user.id, message.message_id - 1)
            driver_doc2 = message.photo[0].file_id
            Work_in_db.add_drive_doc2(message.chat.id, driver_doc2)
            take_photo(message)
        else:
            take_photo(message)
    except TypeError:
        if Work_in_db.user_exists_auto(message.from_user.id)[0][0] is None and \
                Work_in_db.user_exists_drive1(message.from_user.id)[0][0] is None and \
                Work_in_db.user_exists_drive2(message.from_user.id)[0][0] is None:
            if message.text == '0':
                Work_in_db.add_number_phone(message.from_user.id, None)
                start(message)
            else:
                bot.send_message(
                    message.chat.id,
                    f"На данный момент я жду фотографию!")
                take_photo(message)
        else:
            bot.send_message(
                message.chat.id,
                f"На данный момент я жду фотографию!")
            take_photo(message)


def take_photo(mess):
    keyboard = types.InlineKeyboardMarkup()
    back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
    null_num_driver = types.InlineKeyboardButton(text="Введён не правильный номер", callback_data='null_num_driver')
    keyboard.add(back_rooms)
    keyboard.add(null_num_driver)
    if Work_in_db.user_exists_auto(mess.from_user.id)[0][0] is None:
        mem = bot.send_message(
            mess.from_user.id,
            f"Пришлите, пожалуйста, фотографию документа на авто.\n"
            f"Сторона с номером авто",
            reply_markup=keyboard)
        bot.register_next_step_handler(mem, photo)
    elif Work_in_db.user_exists_drive1(mess.from_user.id)[0][0] is None:
        mem = bot.send_message(
            mess.from_user.id,
            f"Пришлите, пожалуйста, фотографию вашего В/У.\n"
            f"Лицевая сторона В/У",
            reply_markup=keyboard)
        bot.register_next_step_handler(mem, photo)
    elif Work_in_db.user_exists_drive2(mess.from_user.id)[0][0] is None:
        mem = bot.send_message(
            mess.from_user.id,
            f"Пришлите, пожалуйста, фотографию вашего В/У.\n"
            f"Обратная сторона В/У",
            reply_markup=keyboard)
        bot.register_next_step_handler(mem, photo)
    else:
        if str(Work_in_db.user_exists_register(mess.from_user.id)[0][0]) == "2":
            med = Work_in_db.user_exists_auto(mess.from_user.id)[0][0]
            bot.send_message(
                mess.from_user.id,
                f"Все отправленные вами фото уже в обработке!\n"
                f"Я вас уведомлю после успешной регистрации\n"
                f"По всем вопросам можете обратиться:\n"
                f"По номеру +{Work_in_db.take_first_admin_num()[0][0]}\n"
                f"Или по ссылке: @{Work_in_db.take_first_admin_name()[0][0]}")
            Work_in_db.save_info(mess.from_user.id,
                                 Work_in_db.exist_number_phone(mess.from_user.id)[0][0],
                                 mess.message_id, 2)
            if Work_in_db.take_user_name(mess.from_user.id)[0][0] is None:
                admins = Work_in_db.take_admin_id()
                mess_admin = []
                for call_admin in admins:
                    if call_admin[4] == '1':
                        mess_admin.append(call_admin)
                if not mess_admin:
                    pass
                else:
                    mes1 = bot.send_message(
                        mess_admin[0][1],
                        f"Заявка на регистрацию нового автомобиля!\n"
                        f"Номер телефона: +{Work_in_db.exist_number_phone(mess.from_user.id)[0][0]}\n")
                    bot.send_photo(
                        mess_admin[0][1],
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        mess_admin[0][1],
                        f"Готово - водитель зарегистрирован (сначала зарегистрировать, потом нажать готово)\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_car_doc())
            else:
                admins = Work_in_db.take_admin_id()
                mess_admin = []
                for call_admin in admins:
                    if call_admin[4] == '1':
                        mess_admin.append(call_admin)
                if not mess_admin:
                    pass
                else:
                    mes1 = bot.send_message(
                        mess_admin[0][1],
                        f"Заявка на регистрацию нового автомобиля!\n"
                        f"Номер телефона: +{Work_in_db.exist_number_phone(mess.from_user.id)[0][0]}\n"
                        f"Ссылка на телеграмм: @{Work_in_db.take_user_name(mess.from_user.id)[0][0]}\n")
                    bot.send_photo(
                        mess_admin[0][1],
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        mess_admin[0][1],
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_car_doc())
        elif str(Work_in_db.user_exists_register(mess.from_user.id)[0][0]) == "3":
            med = [types.InputMediaPhoto(Work_in_db.user_exists_drive2(mess.from_user.id)[0][0]),
                   types.InputMediaPhoto(Work_in_db.user_exists_drive1(mess.from_user.id)[0][0])]
            bot.send_message(
                mess.from_user.id,
                f"Все отправленные вами фото уже в обработке!\n"
                f"Я вас уведомлю после успешной регистрации\n"
                f"По всем вопросам можете обратиться:\n"
                f"По номеру +{Work_in_db.take_first_admin_num()[0][0]}\n"
                f"Или по ссылке: @{Work_in_db.take_first_admin_name()[0][0]}")
            Work_in_db.save_info(mess.from_user.id,
                                 Work_in_db.exist_number_phone(mess.from_user.id)[0][0],
                                 mess.message_id, 3)
            if Work_in_db.take_user_name(mess.from_user.id)[0][0] is None:
                admins = Work_in_db.take_admin_id()
                mess_admin = []
                for call_admin in admins:
                    if call_admin[4] == '1':
                        mess_admin.append(call_admin)
                if not mess_admin:
                    pass
                else:
                    mes1 = bot.send_message(
                        mess_admin[0][1],
                        f"Заявка на регистрацию нового В/У!\n"
                        f"Номер телефона: +{Work_in_db.exist_number_phone(mess.from_user.id)[0][0]}\n")
                    bot.send_media_group(
                        mess_admin[0][1],
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        mess_admin[0][1],
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_driver_doc())
            else:
                admins = Work_in_db.take_admin_id()
                mess_admin = []
                for call_admin in admins:
                    if call_admin[4] == '1':
                        mess_admin.append(call_admin)
                if not mess_admin:
                    pass
                else:
                    mes1 = bot.send_message(
                        mess_admin[0][1],
                        f"Заявка на регистрацию нового В/У!!\n"
                        f"Номер телефона: +{Work_in_db.exist_number_phone(mess.from_user.id)[0][0]}\n"
                        f"Ссылка на телеграмм: @{Work_in_db.take_user_name(mess.from_user.id)[0][0]}\n")
                    bot.send_media_group(
                        mess_admin[0][1],
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        mess_admin[0][1],
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_driver_doc())
        elif Work_in_db.user_exists_register(mess.chat.id)[0][0] is None:
            # med = [types.InputMediaPhoto(Work_in_db.user_exists_drive2(mess.from_user.id)[0][0]),
            #        types.InputMediaPhoto(Work_in_db.user_exists_drive1(mess.from_user.id)[0][0]),
            #        types.InputMediaPhoto(Work_in_db.user_exists_auto(mess.from_user.id)[0][0])]
            # bot.send_message(
            #     mess.from_user.id,
            #     f"Все отправленные вами фото уже в обработке!\n"
            #     f"Я вас уведомлю после успешной регистрации и дам доступ к работе над документами\n"
            #     f"По всем вопросам можете обратиться:\n"
            #     f"По номеру +{Work_in_db.take_first_admin_num()[0][0]}\n"
            #     f"Или по ссылке: @{Work_in_db.take_first_admin_name()[0][0]}", )
            # Work_in_db.save_info(mess.from_user.id,
            #                      Work_in_db.exist_number_phone(mess.from_user.id)[0][0],
            #                      mess.message_id, None)
            welcome_driver(mess)
            #
            # if Work_in_db.take_user_name(mess.from_user.id)[0][0] is None:
            #     admins = Work_in_db.take_admin_id()
            #     mess_admin = []
            #     for call_admin in admins:
            #         if call_admin[4] == '1':
            #             mess_admin.append(call_admin)
            #     if not mess_admin:
            #         pass
            #     else:
            #         mes1 = bot.send_message(
            #             mess_admin[0][1],
            #             f"Заявка на регистрацию водителем!\n"
            #             f"Номер телефона: +{Work_in_db.exist_number_phone(mess.from_user.id)[0][0]}\n")
            #         bot.send_media_group(
            #             mess_admin[0][1],
            #             med,
            #             reply_to_message_id=mes1.message_id, )
            #         bot.send_message(
            #             mess_admin[0][1],
            #             f"Готово - водитель зарегистрирован\n"
            #             f"Отмена - попросим загрузить фото ещё раз",
            #             reply_markup=admin_reg_driver())
            # else:
            #     admins = Work_in_db.take_admin_id()
            #     mess_admin = []
            #     for call_admin in admins:
            #         if call_admin[4] == '1':
            #             mess_admin.append(call_admin)
            #     if not mess_admin:
            #         pass
            #     else:
            #         mes1 = bot.send_message(
            #             mess_admin[0][1],
            #             f"Заявка на регистрацию водителем!\n"
            #             f"Номер телефона: +{Work_in_db.exist_number_phone(mess.from_user.id)[0][0]}\n"
            #             f"Ссылка на телеграмм: @{Work_in_db.take_user_name(mess.from_user.id)[0][0]}\n")
            #         bot.send_media_group(
            #             mess_admin[0][1],
            #             med,
            #             reply_to_message_id=mes1.message_id, )
            #         bot.send_message(
            #             mess_admin[0][1],
            #             f"Готово - водитель зарегистрирован\n"
            #             f"Отмена - попросим загрузить фото ещё раз",
            #             reply_markup=admin_reg_driver())


def take_park_num(message, message_delete):
    number = bot_works.enter_num(message)
    if number is False or number is True:
        bot.delete_message(message.from_user.id, message_delete)
        bot.send_message(message.from_user.id,
                         'Ошибка в номере телефона, попробуйте ещё раз\n',
                         reply_markup=Buttons.back_menu_rooms())
        message_delete = message.message_id + 1
        bot.register_next_step_handler(message, take_park_num, message_delete)
    else:
        try:
            park = settings.URL_PARK[number]
        except KeyError:
            park = None
        bot.delete_message(message.from_user.id, message_delete)
        if not park:
            try:
                print(Buttons.files_park[message.from_user.id])
                print(park)
                bot_works.create_info(message)
            except KeyError:
                if not Parks.park_num_exists(number):
                    Buttons.files_park[message.from_user.id] = {"name_p": None,
                                                                "unp_p": None,
                                                                "num_p": None,
                                                                "email_p": None,
                                                                "address_p": None}
                    bot.send_message(message.from_user.id,
                                     'Номер телефона получен!\n'
                                     'Не вижу вас в базе! Приступим к процедуре регистрации:',
                                     reply_markup=Buttons.enter_park_info())

                else:
                    bot.send_message(message.from_user.id, 'qwer')
        else:
            try:
                Parks.add_park_in_base(message.from_user.id, park)
                bot.send_message(message.from_user.id, 'Вижу вас в базе! Добро пожаловать')
            except:
                bot.send_message(message.from_user.id,
                                 f'Данный номер вам не доступен! Обратитесь к администратору\n'
                                 f'Номер телефона: +{Work_in_db.take_first_admin_num()[0][0]}\n'
                                 f'Ссылка на телеграмм: {Work_in_db.take_first_admin_name()[0][0]}',
                                 reply_markup=Buttons.back_menu_rooms())
                # del Buttons.files_park[message.from_user.id]


@bot.callback_query_handler(func=lambda call: True)
def button_work(call):
    if call.data == "name":
        bot.edit_message_text(message_id=call.message.message_id,
                              chat_id=call.from_user.id,
                              text="Напишите имя организации")
        bot.register_next_step_handler(call.message, bot_works.take_info_park, call.data)
    if call.data == "unp":
        bot.edit_message_text(message_id=call.message.message_id,
                              chat_id=call.from_user.id,
                              text="Напишите ваш УНП")
        bot.register_next_step_handler(call.message, bot_works.take_info_park, call.data)
    if call.data == "num":
        bot.edit_message_text(message_id=call.message.message_id,
                              chat_id=call.from_user.id,
                              text="Номер телефона организации")
        bot.register_next_step_handler(call.message, bot_works.take_info_park, call.data)
    if call.data == "email":
        bot.edit_message_text(message_id=call.message.message_id,
                              chat_id=call.from_user.id,
                              text="Почтовый адрес email")
        bot.register_next_step_handler(call.message, bot_works.take_info_park, call.data)
    if call.data == "address":
        bot.edit_message_text(message_id=call.message.message_id,
                              chat_id=call.from_user.id,
                              text="Адрес регистрации")
        bot.register_next_step_handler(call.message, bot_works.take_info_park, call.data)
    if call.data == 'back_reg':
        bot.edit_message_text(message_id=call.message.message_id,
                              chat_id=call.from_user.id,
                              text="Выберите пункт для изменения:",
                              reply_markup=Buttons.enter_park_info())

    if call.data == "reg_driver":
        if not Work_in_db.user_exists(call.from_user.id):
            '''eсть ли юзер в базе, если нету, то создаём (сохраняет и id юзера и его имя аккаунта(если есть)'''
            Work_in_db.add_user(call.from_user.id, call.from_user.username)
        if not Work_in_db.user_exists_name(call.from_user.username):
            '''проверяем не сменил ли юзер имя аккаунта телеги, если да, то меняем'''
            Work_in_db.change_user_name(call.from_user.username, call.from_user.id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                text=f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                     f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            if Work_in_db.user_exists_auto(call.from_user.id)[0][0] is not None and \
                    Work_in_db.user_exists_drive1(call.from_user.id)[0][0] is not None and \
                    Work_in_db.user_exists_drive2(call.from_user.id)[0][0] is not None:
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text='Все документы уже были получены!\n'
                         'Мы можем предложить вам тарифы "Майфлит"(ИП) и "Драйв"(физ)\n '
                         ' \n'
                         'Либо "Смартдрайв" - парк на выбор, '
                         'при подключении к парку комиссия арми 0%:\n',
                    reply_markup=Buttons.menu_districts())
            else:
                if Work_in_db.exist_number_phone(call.from_user.id)[0][0] is None:
                    keyboard = types.InlineKeyboardMarkup()
                    back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
                    keyboard.add(back_rooms)
                    bot.edit_message_text(chat_id=call.from_user.id,
                                          message_id=call.message.message_id,
                                          text='Введите Ваш рабочий номер телефона\n'
                                               ' \n'
                                               'Пример: 375 ** *******',
                                          reply_markup=keyboard)
                    bot.register_next_step_handler(call.message, enter_chat_number)
                else:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    take_photo(call)

    if call.data == 'reg_park':
        keyboard = types.InlineKeyboardMarkup()
        back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
        keyboard.add(back_rooms)
        print(call.from_user.id)
        print(Parks.park_exists(call.from_user.id))
        if not Parks.park_exists(call.from_user.id):
            bot.edit_message_text(chat_id=call.from_user.id,
                                  message_id=call.message.message_id,
                                  text='Введите рабочий номер телефона организации\n'
                                       ' \n'
                                       'Пример: 375 ** *******',
                                  reply_markup=keyboard)
            message_delete = call.message.message_id
            bot.register_next_step_handler(call.message, take_park_num, message_delete)
        else:
            info_park = Parks.take_park_info(call.from_user.id)
            if not info_park:
                bot.edit_message_text(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      text=f'Приступим к процедуре регистрации')
            else:
                bot.edit_message_text(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      text=f'Добро пожаловать!\n'
                                           f'Ваш парк: {info_park[0][2]}\n'
                                           f'Ваш номер: {info_park[0][4]}\n'
                                           f'Ваш email: {info_park[0][5]}\n'
                                           f'Ваш УНП: {info_park[0][3]}\n'
                                           f'Ваш адрес: {info_park[0][6]}')

    if call.data == 'null_num_driver':
        bot.clear_step_handler_by_chat_id(call.from_user.id)
        Blocks.back_menu(call)
        Work_in_db.delete_all_driver(call.from_user.id)

    if call.data == 'back_rooms':
        bot.clear_step_handler_by_chat_id(call.from_user.id)
        Blocks.back_menu(call)

    if call.data == 'park':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='*"Смартдрайв" - парк на выбор*\n'
                                   ' \n'
                                   '\u2705 Комиссия ARMI 0%\n'
                                   '\u2705 Комиссия партнёра до 15%\n'
                                   '\u2705 Ежедневные выплаты\n'
                                   '\u2705 Официальное трудоустройство\n'
                                   'Выберите район:',
                              parse_mode='Markdown',
                              reply_markup=buttons.districts1())

    if call.data == 'up':
        mes = call.message.json['reply_markup']['inline_keyboard'][1][0]['text']
        Blocks.up(call, mes)

    if call.data == 'down':
        mes = call.message.json['reply_markup']['inline_keyboard'][1][0]['text']
        Blocks.down(call.message, mes)

    if call.data == 'my_flit':
        keyboard = types.InlineKeyboardMarkup()
        add_my_flit_tariff = types.InlineKeyboardButton(text="Подключиться", callback_data='add_my_flit_tariff')
        drive = types.InlineKeyboardButton(text="Драйв", callback_data='drive')
        park = types.InlineKeyboardButton(text="Выбрать парк", callback_data='park')
        back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
        keyboard.add(add_my_flit_tariff)
        keyboard.add(drive)
        keyboard.add(park)
        keyboard.add(back_rooms)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='*Для организаций и индивидуальных предпринимателей*\n'
                                   ' \n'
                                   '\u2705 Комиссия ARMI 7%\n'
                                   '\u2705 Эквайринг 1,6-2,8%\n',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'drive':
        keyboard = types.InlineKeyboardMarkup()
        add_my_flit = types.InlineKeyboardButton(text="Подключиться", callback_data='add_drive_tariff')
        my_flit = types.InlineKeyboardButton(text="Майфлит", callback_data='my_flit')
        park = types.InlineKeyboardButton(text="Выбрать парк", callback_data='park')
        back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
        keyboard.add(add_my_flit)
        keyboard.add(my_flit)
        keyboard.add(park)
        keyboard.add(back_rooms)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='*Специальная программа для водителей ARMI*\n'
                                   ' \n'
                                   '\u2705 Абонентская плата $15/месяц\n'
                                   '\u2705 Комиссия арми 0%\n'
                                   '\u2705 Заправка с баланса\n'
                                   '\u2705 Без привязки к парку\n'
                                   '\u2705 Моментальные выплаты\n',
                              parse_mode='Markdown',
                              reply_markup=keyboard)

    if call.data == 'add_new_num':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        try:
            url = requests.get(f'{settings.URL}{Work_in_db.take_user_num_info(call.message.id - 2)[0][0]}')
            try:
                Work_in_db.add_num_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0],
                                       url.json()['car']['regNumber'])
            except TypeError:
                Work_in_db.add_num_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0], None)
            try:
                Work_in_db.add_name_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0],
                                        url.json()['car']['automaker'])
            except TypeError:
                Work_in_db.add_name_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0], None)
            try:
                Work_in_db.add_model_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0],
                                         url.json()['car']['model'])
            except TypeError:
                Work_in_db.add_model_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0], None)
            Work_in_db.add_number_phone(Work_in_db.take_user_id_info(call.message.id - 2)[0][0],
                                        Work_in_db.take_user_num_info(call.message.id - 2)[0][0])
            bot.send_message(call.from_user.id, "Водитель был уведомлен об успешной смене номера!")
            bot.send_message(Work_in_db.take_user_id_info(call.message.id - 2)[0][0],
                             f"Номер телефона успешно изменён!\n"
                             f"Ваш номер телефона: +{Work_in_db.exist_number_phone(Work_in_db.take_user_id_info(call.message.id - 2)[0][0])[0][0]}\n"
                             f"Ваша машина: {Work_in_db.take_name_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0])[0][0]} "
                             f"{Work_in_db.take_model_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0])[0][0]}, номер машины: "
                             f"{Work_in_db.take_num_car(Work_in_db.take_user_id_info(call.message.id - 2)[0][0])[0][0]}")
            Work_in_db.delete_info_money(call.message.id - 2)
        except IndexError:
            info = Work_in_db.take_all_info()
            reg_info = []
            for all_info in info:
                if all_info[-3] == '10':
                    reg_info.append(all_info)
            url = requests.get(f'{settings.URL}{reg_info[0][2]}')
            try:
                Work_in_db.add_num_car(reg_info[0][1], url.json()['car']['regNumber'])
            except TypeError:
                Work_in_db.add_num_car(reg_info[0][1], None)
            try:
                Work_in_db.add_name_car(reg_info[0][1], url.json()['car']['automaker'])
            except TypeError:
                Work_in_db.add_name_car(reg_info[0][1], None)
            try:
                Work_in_db.add_model_car(reg_info[0][1], url.json()['car']['model'])
            except TypeError:
                Work_in_db.add_model_car(reg_info[0][1], None)
            Work_in_db.add_number_phone(reg_info[0][1], reg_info[0][-1])
            bot.send_message(reg_info[0][1], "Водитель был уведомлен об успешной смене номера!")
            bot.send_message(reg_info[0][1],
                             f"Номер телефона успешно изменён!\n"
                             f"Ваш номер телефона: +{reg_info[0][-1]}\n"
                             f"Ваша машина: {Work_in_db.take_name_car(reg_info[0][1])[0][0]} "
                             f"{Work_in_db.take_model_car(reg_info[0][1])[0][0]}, номер машины: "
                             f"{Work_in_db.take_num_car(reg_info[0][1])[0][0]}")
            Work_in_db.delete_info_money(reg_info[0][0])

    if call.data == 'my_info':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            url = requests.get(f'{settings.URL}{Work_in_db.exist_number_phone(call.from_user.id)[0][0]}')
            try:
                Work_in_db.add_num_car(call.from_user.id, url.json()['car']['regNumber'])
            except TypeError:
                Work_in_db.add_num_car(call.from_user.id, None)
            try:
                Work_in_db.add_name_car(call.from_user.id, url.json()['car']['automaker'])
            except TypeError:
                Work_in_db.add_name_car(call.from_user.id, None)
            try:
                Work_in_db.add_model_car(call.from_user.id, url.json()['car']['model'])
            except TypeError:
                Work_in_db.add_model_car(call.from_user.id, None)
            welcome_driver(call)

    if call.data == 'exists_admin':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            call.message.chat.id,
            f"\u2705 Администратор запросов - "
            f"получает все уведомления при получении запросов на смену/регистрацию документов\n"
            f"\u2705 Администратор безнала - получает все уведомления по запросам перевода безнала на баланс\n"
            f"\u2705 Администратор контактов - его контактные данные будут передаваться для связи",
            reply_markup=(admin_reg()))

    if call.data == 'not_drive':
        list_doc = []
        bot.delete_message(call.message.chat.id, call.message.message_id)
        for i in Work_in_db.take_all():
            if i[-1] is None or str(i[-1]) == "2" or str(i[-1]) == "3":
                if Work_in_db.user_exists_auto(i[1])[0][0] is not None and \
                        Work_in_db.user_exists_drive1(i[1])[0][0] is not None and \
                        Work_in_db.user_exists_drive2(i[1])[0][0] is not None:
                    list_doc.append(i)
                else:
                    pass
        if len(list_doc) == 0:
            bot.send_message(
                call.message.chat.id,
                f"Документы на одобрение отсутствуют!\n",
                reply_markup=admin_button())

        if len(list_doc) != 0:
            med = [types.InputMediaPhoto(list_doc[0][7]),
                   types.InputMediaPhoto(list_doc[0][6]),
                   types.InputMediaPhoto(list_doc[0][5])]
            if list_doc[0][2] is None:
                id_tele.append(list_doc[0][1])
                if list_doc[0][-1] is None:
                    mes1 = bot.send_message(
                        call.message.chat.id,
                        f"Заявка на регистрацию водителем!\n"
                        f"Номер телефона: +{list_doc[0][4]}\n")
                    bot.send_media_group(
                        call.message.chat.id,
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        call.message.chat.id,
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_reg_driver())
                elif str(list_doc[0][-1]) == '2':
                    mes1 = bot.send_message(
                        call.message.chat.id,
                        f"Заявка на смену документа автомобиля!\n"
                        f"Номер телефона: +{list_doc[0][4]}\n")
                    bot.send_photo(
                        call.message.chat.id,
                        list_doc[0][7],
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        call.message.chat.id,
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_car_doc())
                elif str(list_doc[0][-1]) == '3':
                    med = [types.InputMediaPhoto(list_doc[0][6]),
                           types.InputMediaPhoto(list_doc[0][5])]
                    mes1 = bot.send_message(
                        call.message.chat.id,
                        f"Заявка на смену В/У!\n"
                        f"Номер телефона: +{list_doc[0][4]}\n")
                    bot.send_media_group(
                        call.message.chat.id,
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        call.message.chat.id,
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_driver_doc())

            else:
                id_tele.append(list_doc[0][1])
                if list_doc[0][-1] is None:
                    mes1 = bot.send_message(
                        call.message.chat.id,
                        f"Заявка на регистрацию водителем!\n"
                        f"Ссылка на телеграмм: @{list_doc[0][2]}\n"
                        f"Номер телефона: +{list_doc[0][4]}\n")
                    bot.send_media_group(
                        call.message.chat.id,
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        call.message.chat.id,
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_reg_driver())
                elif str(list_doc[0][-1]) == '2':
                    mes1 = bot.send_message(
                        call.message.chat.id,
                        f"Заявка на смену документа автомобиля!\n"
                        f"Номер телефона: +{list_doc[0][4]}\n")
                    bot.send_photo(
                        call.message.chat.id,
                        list_doc[0][7],
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        call.message.chat.id,
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_car_doc())
                elif str(list_doc[0][-1]) == '3':
                    med = [types.InputMediaPhoto(list_doc[0][6]),
                           types.InputMediaPhoto(list_doc[0][5])]
                    mes1 = bot.send_message(
                        call.message.chat.id,
                        f"Заявка на смену В/У!\n"
                        f"Номер телефона: +{list_doc[0][4]}\n")
                    bot.send_media_group(
                        call.message.chat.id,
                        med,
                        reply_to_message_id=mes1.message_id, )
                    bot.send_message(
                        call.message.chat.id,
                        f"Готово - водитель зарегистрирован\n"
                        f"Отмена - попросим загрузить фото ещё раз",
                        reply_markup=admin_change_driver_doc())

    if call.data == "back_menu":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            call.message.chat.id,
            f"Возвращаемся в меню администратора",
            reply_markup=admin_button())

    if call.data == "next_reg_driver":
        bot.edit_message_text(message_id=call.message.message_id,
                              chat_id=call.from_user.id,
                              text='Данные сохранены и отправлены администратору, '
                                   'я дам вам обратную связь по завершению регистрации!')
        Parks.add_park_in_base(id_park=call.from_user.id,
                               info_park=Buttons.files_park[call.from_user.id])

    if call.data == "add_driver":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 4)
        if not id_tele:
            bot.send_message(
                call.message.chat.id,
                f"Водителю отправлено письмо об успешной регистрации!")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Водителю отправлено письмо об успешной регистрации!",
                reply_markup=next_reg_driver())
        if not id_tele:
            try:
                Work_in_db.add_armi_driver(Work_in_db.take_user_id_info(call.message.message_id - 7)[0][0], "0")
                bot.send_message(
                    Work_in_db.take_user_id_info(call.message.message_id - 7)[0][0],
                    f"Регистрация успешно пройдена! \n"
                    f"Теперь вам доступен личный кабинет бота и доступ в приложение такси ARMI", )
                call.from_user.id = Work_in_db.take_user_id_info(call.message.message_id - 7)[0][0]
                print(call)
                welcome_driver(call)
                Work_in_db.delete_info(Work_in_db.take_user_id_info(call.message.message_id - 7)[0][0])
            except IndexError:
                bot.send_message(
                    call.from_user.id,
                    f"Какой-то из админов уже закрыл эту заявку \n")
        else:
            Work_in_db.add_armi_driver(id_tele[0], '0')
            bot.send_message(
                id_tele[0],
                f"Регистрация успешно пройдена! \n"
                f"Теперь вам доступен личный кабинет бота и доступ в приложение такси ARMI", )
            call.from_user.id = id_tele[0]
            print(call)
            welcome_driver(call)

            Work_in_db.delete_info(id_tele[0])
            id_tele.clear()

    if call.data == "otmena":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.clear_step_handler_by_chat_id(call.from_user.id)
        bot.send_message(call.from_user.id,
                         'ydalil',
                         reply_markup=Buttons.if_not_drive())

    if call.data == "add_car_doc":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        if not id_tele:
            bot.send_message(
                call.message.chat.id,
                f"Водителю отправлено письмо об успешной регистрации!")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Водителю отправлено письмо об успешной регистрации!",
                reply_markup=next_reg_driver())
        if not id_tele:
            Work_in_db.add_armi_driver(Work_in_db.take_user_id_info(call.message.message_id - 5)[0][0], "0")
            bot.send_message(
                Work_in_db.take_user_id_info(call.message.message_id - 5)[0][0],
                f"Регистрация документа на авто успешно пройдена!\n"
                f"Теперь в приложении такси ARMI у вас новый автомобиль!",
                reply_markup=room_for_driver())
            Work_in_db.delete_info_money(call.message.message_id - 5)
        else:
            Work_in_db.add_armi_driver(id_tele[0], '0')
            bot.send_message(
                id_tele[0],
                f"Регистрация документа на авто успешно пройдена!\n"
                f"Теперь в приложении такси ARMI у вас новый автомобиль!",
                reply_markup=room_for_driver())
            for info in Work_in_db.take_all_info_id(id_tele[0]):
                if info[3] != "5" and info[3] != "10":
                    Work_in_db.delete_info_money(info[0])
            id_tele.clear()

    if call.data == "add_driver_doc":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        if not id_tele:
            bot.send_message(
                call.message.chat.id,
                f"Водителю отправлено письмо об успешной регистрации!")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Водителю отправлено письмо об успешной регистрации!",
                reply_markup=next_reg_driver())
        if not id_tele:
            Work_in_db.add_armi_driver(Work_in_db.take_user_id_info(call.message.message_id - 6)[0][0], "0")
            bot.send_message(
                Work_in_db.take_user_id_info(call.message.message_id - 6)[0][0],
                f"Регистрация новых документов на авто успешно пройдена!\n"
                f"Теперь в приложении такси ARMI у вас новый автомобиль!",
                reply_markup=room_for_driver())
            Work_in_db.delete_info_money(call.message.message_id - 6)
        else:
            Work_in_db.add_armi_driver(id_tele[0], '0')
            bot.send_message(
                id_tele[0],
                f"Регистрация нового В/У успешно пройдена!\n"
                f"Теперь к приложению такси ARMI у вас привязаны новое В/У!",
                reply_markup=room_for_driver())
            for info in Work_in_db.take_all_info_id(id_tele[0]):
                if info[3] != "5" and info[3] != "10":
                    Work_in_db.delete_info_money(info[0])
            id_tele.clear()

    if call.data == 'backup_car_doc':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        if not id_tele:
            bot.send_message(
                call.message.chat.id,
                f"Фотография удалена, попросим прислать ещё раз!")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Фотография удалена, попросим прислать ещё раз!",
                reply_markup=next_reg_driver())
        if not id_tele:
            Work_in_db.del_doc_car(Work_in_db.take_user_id_info(call.message.message_id - 5)[0][0])
            bot.send_message(
                Work_in_db.take_user_id_info(call.message.message_id - 5)[0][0],
                f"Ваша заявка на регистрацию новой машины была отклонена.\n"
                f"Попробуйте прислать фото ещё раз, возможно, дело в их качестве\n"
                f"По всем вопросам: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}",
                reply_markup=room_for_driver_reg2())
            Work_in_db.delete_info(Work_in_db.take_user_id_info(call.message.message_id - 5)[0][0])
        else:
            Work_in_db.del_doc_car(id_tele[0])
            bot.send_message(
                id_tele[0],
                f"Ваша заявка на регистрацию новой машины была отклонена.\n"
                f"Попробуйте прислать фото ещё раз, возможно, дело в их качестве\n"
                f"По всем вопросам: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}",
                reply_markup=room_for_driver_reg2())
            id_tele.clear()

    if call.data == 'backup_new_num':
        try:
            num = Work_in_db.take_user_num_info(call.message.id - 2)[0][0]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.from_user.id,
                             "Водитель уведомлен об отказе в регистрации!")
            bot.send_message(Work_in_db.take_user_id_info(call.message.id - 2)[0][0],
                             f"Вам отказано в регистрации нового номера! \n"
                             f"По всем вопросам можете обратиться: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                             f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}", )
            Work_in_db.delete_info_money(int(call.message.id - 2))
        except IndexError:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            info = Work_in_db.take_all_info()
            reg_info = []
            for all_info in info:
                if all_info[-3] == '10':
                    reg_info.append(all_info)
            try:
                Work_in_db.delete_info_money(reg_info[0][0])
                bot.send_message(call.from_user.id,
                                 "Водитель уведомлен об отказе в регистрации!",
                                 reply_markup=admin_button())
                bot.send_message(reg_info[0][1],
                                 f"Вам отказано в регистрации нового номера! \n"
                                 f"По всем вопросам можете обратиться: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                                 f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}", )
            except IndexError:
                bot.send_message(call.from_user.id,
                                 f"Какой-то из админов уже принял решение по этому запросу! Проверьте правильность", )

    if call.data == 'backup_driver_doc':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        if not id_tele:
            bot.send_message(
                call.message.chat.id,
                f"Фотографии удалены, попросим прислать ещё раз!")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Фотографии удалены, попросим прислать ещё раз!",
                reply_markup=next_reg_driver())
        if not id_tele:
            Work_in_db.del_doc_driver(Work_in_db.take_user_id_info(call.message.message_id - 6)[0][0])
            bot.send_message(
                Work_in_db.take_user_id_info(call.message.message_id - 6)[0][0],
                f"Ваша заявка на регистрацию нового В/У была отклонена.\n"
                f"Попробуйте прислать фото ещё раз, возможно, дело в их качестве\n"
                f"По всем вопросам: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}",
                reply_markup=room_for_driver_reg3())
            Work_in_db.delete_info_money(call.message.message_id - 6)
        else:
            Work_in_db.del_doc_driver(id_tele[0])
            bot.send_message(
                id_tele[0],
                f"Ваша заявка на регистрацию нового В/У была отклонена.\n"
                f"Попробуйте прислать фото ещё раз, возможно, дело в их качестве\n"
                f"По всем вопросам: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}",
                reply_markup=room_for_driver_reg3())
            for info in Work_in_db.take_all_info_id(id_tele[0]):
                if info[3] != "5" and info[3] != "10":
                    Work_in_db.delete_info_money(info[0])
            id_tele.clear()

    if call.data == 'backup_driver':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 4)
        if not id_tele:
            bot.send_message(
                call.message.chat.id,
                f"Фотографии удалены, попросим прислать ещё раз!")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Фотографии удалены, попросим прислать ещё раз!",
                reply_markup=next_reg_driver())
        if not id_tele:
            try:
                Work_in_db.del_doc(Work_in_db.take_user_id_info(call.message.message_id - 7)[0][0])
                bot.send_message(
                    Work_in_db.take_user_id_info(call.message.message_id - 7)[0][0],
                    f"Ваша заявка на регистрацию была отклонена.\n"
                    f"Попробуйте прислать фото ещё раз, возможно, дело в их качестве\n"
                    f"По всем вопросам: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                    f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}",
                    reply_markup=Buttons.if_not_drive())
                Work_in_db.delete_info_money(call.message.message_id - 7)
            except IndexError:
                bot.send_message(
                    call.from_user.id,
                    f"Какой-то из админов уже отклонил эту заявку \n")
        else:
            Work_in_db.del_doc(id_tele[0])
            bot.send_message(
                id_tele[0],
                f"Ваша заявка на регистрацию была отклонена.\n"
                f"Попробуйте прислать фото ещё раз, возможно, дело в их качестве\n"
                f"По всем вопросам: @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по номеру телефона: +{Work_in_db.take_first_admin_num()[0][0]}",
                reply_markup=Buttons.if_not_drive())
            for info in Work_in_db.take_all_info_id(id_tele[0]):
                if info[3] != "5" and info[3] != "10":
                    Work_in_db.delete_info_money(info[0])
            id_tele.clear()

    if call.data == "later_driver":
        if not id_tele:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.delete_message(call.message.chat.id, call.message.message_id - 2)
            bot.delete_message(call.message.chat.id, call.message.message_id - 3)
            bot.delete_message(call.message.chat.id, call.message.message_id - 4)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.delete_message(call.message.chat.id, call.message.message_id - 2)
            bot.delete_message(call.message.chat.id, call.message.message_id - 3)
            bot.delete_message(call.message.chat.id, call.message.message_id - 4)
            bot.send_message(call.from_user.id, 'Возвращаемся в меню администратора',
                             reply_markup=admin_button())

    if call.data == "later_car_doc":
        if not id_tele:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.delete_message(call.message.chat.id, call.message.message_id - 2)
            bot.send_message(call.from_user.id, 'Возвращаемся в меню администратора',
                             reply_markup=admin_button())

    if call.data == "later_driver_doc":
        if not id_tele:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.delete_message(call.message.chat.id, call.message.message_id - 2)
            bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.delete_message(call.message.chat.id, call.message.message_id - 2)
            bot.delete_message(call.message.chat.id, call.message.message_id - 3)
            bot.send_message(call.from_user.id, 'Возвращаемся в меню администратора',
                             reply_markup=admin_button())

    if call.data == "later_money_balance":
        if not need_money_balance:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            need_money_balance.clear()
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            need_money_balance.clear()
            bot.send_message(call.from_user.id, 'Возвращаемся в меню администратора',
                             reply_markup=admin_button())

    if call.data == "later_driver_num":
        try:
            num = Work_in_db.take_user_num_info(call.message.id - 2)[0][0]
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except IndexError:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.from_user.id, "Возвращаемся в меню!",
                             reply_markup=admin_button())

    if call.data == "new_admin":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        mess = bot.send_message(
            call.message.chat.id,
            f"Введите ID аккаунта телеграмм\n"
            f"Если передумали, введите 0", )
        bot.register_next_step_handler(mess, add_admin)

    if call.data == 'new_num_admin':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        mess = bot.send_message(
            call.message.chat.id,
            f"Введите новый номер телефона\n"
            f"Ваш текущий номер телефона: +{Work_in_db.take_admin_num(call.from_user.id)[0][0]}\n"
            f"Если вы передумали, напишите 0!", )
        bot.register_next_step_handler(mess, change_number_admin)

    if call.data == 'new_num_driver':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            if Work_in_db.exist_new_num_driver_user(call.from_user.id) is True:
                bot.send_message(call.from_user.id,
                                 'Ожидайте подтверждения регистрации нового номера! Я вас уведомлю!',
                                 reply_markup=room_for_driver())
            else:
                mess = bot.send_message(
                    call.message.chat.id,
                    f"Введите новый номер телефона\n"
                    f"Ваш текущий номер телефона: +{Work_in_db.exist_number_phone(call.from_user.id)[0][0]}\n"
                    f"Если вы передумали, напишите 0!", )
                bot.register_next_step_handler(mess, change_number_driver)

    if call.data == 'new_car_driver':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Подтвердите, что вы хотите изменить данные машины\n"
                f"\u2757\ufe0f\u2757\ufe0f\u2757\ufe0f ВНИМАНИЕ \u2757\ufe0f\u2757\ufe0f\u2757\ufe0f \n"
                f"После подтверждения откатиться нельзя, нужно будет закончить отправку фотографий до конца!",
                reply_markup=yes_no_new_car())

    if call.data == 'new_doc_driver':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Подтвердите, что вы хотите изменить В/У\n"
                f"\u2757\ufe0f\u2757\ufe0f\u2757\ufe0f ВНИМАНИЕ \u2757\ufe0f\u2757\ufe0f\u2757\ufe0f \n"
                f"После подтверждения откатиться нельзя, нужно будет закончить отправку фотографий до конца!",
                reply_markup=yes_no_new_boc())

    if call.data == "no_new_doc":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            if str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) == "2":
                bot.send_message(
                    call.message.chat.id,
                    f"Регистрация отменена!",
                    reply_markup=room_for_driver_reg2())
            if str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) == "3":
                bot.send_message(
                    call.message.chat.id,
                    f"Регистрация отменена!",
                    reply_markup=room_for_driver_reg3())
            if str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) == "0":
                bot.send_message(
                    call.message.chat.id,
                    f"Регистрация отменена!",
                    reply_markup=room_for_driver())

    if call.data == "no_new_car":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            bot.send_message(
                call.message.chat.id,
                f"Регистрация отменена!",
                reply_markup=room_for_driver())

    if call.data == "yes_new_doc":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            if str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) == "2":
                bot.send_message(
                    call.message.chat.id,
                    f"Дождитесь или завершите регистрацию других документов!",
                    reply_markup=room_for_driver())
            elif str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) != "2":
                if str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) == "3" and \
                        Work_in_db.user_exists_drive1(call.message.chat.id)[0][0] is not None and \
                        Work_in_db.user_exists_drive2(call.message.chat.id)[0][0] is not None:
                    bot.send_message(
                        call.message.chat.id,
                        f"Все отправленные вами фото уже в обработке!\n"
                        f"Я вас уведомлю после успешной регистрации\n"
                        f"По всем вопросам можете обратиться:\n"
                        f"По номеру +{Work_in_db.take_first_admin_num()[0][0]}\n"
                        f"Или по ссылке: @{Work_in_db.take_first_admin_name()[0][0]}",
                        reply_markup=room_for_driver_reg3())
                else:
                    Work_in_db.del_doc_driver(call.message.chat.id, None)
                    Work_in_db.add_user_register(call.message.chat.id, 3)
                    take_photo(call)

    if call.data == "yes_new_car":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            if str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) == "3":
                bot.send_message(
                    call.message.chat.id,
                    f"Дождитесь или завершите регистрацию других документов!",
                    reply_markup=room_for_driver())
            elif str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) != "3":
                if str(Work_in_db.user_exists_register(call.message.chat.id)[0][0]) == "2" and \
                        Work_in_db.user_exists_auto(call.message.chat.id)[0][0] is not None:
                    bot.send_message(
                        call.message.chat.id,
                        f"Все отправленные вами фото уже в обработке!\n"
                        f"Я вас уведомлю после успешной регистрации\n"
                        f"По всем вопросам можете обратиться:\n"
                        f"По номеру +{Work_in_db.take_first_admin_num()[0][0]}\n"
                        f"Или по ссылке: @{Work_in_db.take_first_admin_name()[0][0]}",
                        reply_markup=room_for_driver_reg2())
                else:
                    mess = bot.send_message(
                        call.message.chat.id,
                        f"Регистрируем новый автомобиль!")
                    Work_in_db.del_doc_car(mess.chat.id, None)
                    Work_in_db.add_user_register(mess.chat.id, 2)
                    take_photo(call)

    if call.data == "backup_money_balance":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if not need_money_balance:
            bot.send_message(call.from_user.id,
                             "Водителю отправлено сообщение об отказе в переводе средств")
            bot.send_message(Work_in_db.take_user_id_info(call.message.message_id - 2)[0][0],
                             f"Запрос на перевод денежных средств был отклонён. \n"
                             f"Возможно, вы ввели сумму выше вашего безнала\n"
                             f"По всем вопросам можете обратиться по номеру "
                             f"+{Work_in_db.take_first_admin_num()[0][0]}\n"
                             f"Или по ссылке: @{Work_in_db.take_first_admin_name()[0][0]}")
            Work_in_db.delete_info_money(call.message.message_id - 2)
        else:
            bot.send_message(call.from_user.id,
                             "Водителю отправлено сообщение об отказе в переводе средств",
                             reply_markup=next_need_money())
            bot.send_message(need_money_balance[-1][1],
                             f"Запрос на перевод денежных средств был отклонён. \n"
                             f"Возможно, вы ввели сумму выше вашего безнала\n"
                             f"По всем вопросам можете обратиться по номеру "
                             f"+{Work_in_db.take_first_admin_num()[0][0]}\n"
                             f"Или по ссылке: @{Work_in_db.take_first_admin_name()[0][0]}")
            Work_in_db.delete_info_money(need_money_balance[-1][0])
            need_money_balance.clear()

    if call.data == "money_ty_balance":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.user_exists_register(call.from_user.id)[0][0] == "404":
            bot.send_message(
                call.chat.id,
                f"Вы заблокированы, обратитесь к администратору @{Work_in_db.take_first_admin_name()[0][0]}\n"
                f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}")
        else:
            try:
                chest = []
                all_info = Work_in_db.take_all_info_id(call.from_user.id)
                if not all_info:
                    money = bot.send_message(call.from_user.id,
                                             "Введите сумму, которую хотите перевести на баланс (только цифры)\n"
                                             "Введите 0 для отмены!")
                    bot.register_next_step_handler(money, money_balance)
                else:
                    for info in all_info:
                        if info[3] == "5":
                            chest.append(info)
                        if not chest:
                            money = bot.send_message(call.from_user.id,
                                                     "Введите сумму, которую хотите перевести на баланс "
                                                     "(только цифры)\n"
                                                     "Введите 0 для отмены!")
                            bot.register_next_step_handler(money, money_balance)
                        else:
                            bot.send_message(call.from_user.id,
                                             "Заявка на перевод уже создана. Я вас уведомлю по рассмотрению заявки",
                                             reply_markup=room_for_driver())

            except IndexError:
                money = bot.send_message(call.from_user.id,
                                         "Введите сумму, которую хотите перевести на баланс (только цифры)\n"
                                         "Введите 0 для отмены!")
                bot.register_next_step_handler(money, money_balance)

    if call.data == "not_money":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if not Work_in_db.take_all_info():
            bot.send_message(
                call.from_user.id,
                f"Отсутствуют заявки на пополнение баланса!",
                reply_markup=admin_button())
        else:
            for reg_money in Work_in_db.take_all_info():
                if reg_money[3] == "5":
                    need_money_balance.append(reg_money)
            if not need_money_balance:
                bot.send_message(
                    call.from_user.id,
                    f"Отсутствуют заявки на пополнение баланса!",
                    reply_markup=admin_button())
            else:
                if Work_in_db.take_user_name(need_money_balance[-1][1])[0][0] is None:
                    bot.send_message(
                        call.from_user.id,
                        f"Заявка на перевод денег на баланс!\n"
                        f"Номер телефона: +{need_money_balance[-1][2]}\n"
                        f"Просят перевести с безнала на баланс:\n"
                        f"{need_money_balance[-1][4]} рублей",
                        reply_markup=admin_money_balance())
                elif Work_in_db.take_user_name(need_money_balance[-1][1])[0][0] is not None:
                    bot.send_message(
                        call.from_user.id,
                        f"Заявка на перевод денег на баланс!\n"
                        f"Номер телефона: +{need_money_balance[-1][2]}\n"
                        f"Ссылка на телеграмм: @{Work_in_db.take_user_name(need_money_balance[-1][1])[0][0]}\n"
                        f"Просят перевести с безнала на баланс:\n"
                        f"{need_money_balance[-1][4]} рублей",
                        reply_markup=admin_money_balance())

    if call.data == "add_money_balance":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if not need_money_balance:
            bot.send_message(call.from_user.id, "Водителю отправлено письмо о успешном переводе!")
            bot.send_message(Work_in_db.take_user_id_info(call.message.message_id - 2)[0][0],
                             "Средства успешно зачислены на баланс!")
            Work_in_db.delete_info_money(call.message.message_id - 2)
        else:
            print(need_money_balance)
            bot.send_message(call.from_user.id, "Водителю отправлено письмо о успешном переводе!",
                             reply_markup=next_need_money())
            bot.send_message(need_money_balance[0][1],
                             "Средства успешно зачислены на баланс!")
            Work_in_db.delete_info_money(need_money_balance[0][0])
            need_money_balance.clear()

    if call.data == 'new_reg_num_driver':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        info = Work_in_db.take_all_info()
        reg_info = []
        if not info:
            bot.send_message(call.from_user.id,
                             'Запросы на смену номера телефона отсутствуют!',
                             reply_markup=admin_button())
        else:
            if not reg_info:
                bot.send_message(call.from_user.id,
                                 'Запросы на смену номера телефона отсутствуют!',
                                 reply_markup=admin_button())
            else:
                for all_info in info:
                    if all_info[-3] == '10':
                        reg_info.append(all_info)
                bot.send_message(
                    call.from_user.id,
                    f"Запрос на смену номера телефона!\n"
                    f"Старый номер телефона: +{reg_info[0][2]}\n"
                    f"Новый номер телефона: +{reg_info[0][-1]}",
                    reply_markup=admin_change_num_driver_phone())

    if call.data == 'admin_reg_for_docks':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.exist_admin_reg_docks() is False:
            Work_in_db.add_reg_for_docks_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "На данный момент на эту роль никто не назначен! Я назначаю вас. \n"
                             "Для смены роли попросите назначиться другому админу",
                             reply_markup=admin_button())
        else:
            bot.send_message(call.from_user.id,
                             "Администратор уже назначен. Хотите занять его роль? \n",
                             reply_markup=yes_no_admin_reg_doc())

    if call.data == 'yes_reg_admin_docks':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        reg = Work_in_db.take_admin_id()
        admins = []
        for num_reg in reg:
            if num_reg[-3] == '1':
                admins.append(num_reg)
        if not admins:
            Work_in_db.add_reg_for_docks_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "Теперь вы администратор по заявкам \n",
                             reply_markup=admin_button())
        else:
            bot.send_message(Work_in_db.take_first_admin_id(),
                             f"Вы больше не являетесь администратором по заявкам!\n"
                             f"Новый администратор по заявкам: @{Work_in_db.take_name_admin(call.from_user.id)}")
            Work_in_db.add_reg_for_docks_admin(admins[0][1], None)
            Work_in_db.add_reg_for_docks_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "Теперь вы администратор по заявкам \n",
                             reply_markup=admin_button())

    if call.data == 'admin_reg_for_cash':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.exist_admin_reg_cash() is False:
            Work_in_db.add_reg_for_cash_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "На данный момент на эту роль никто не назначен! Я назначаю вас. \n"
                             "Для смены роли попросите назначиться другому админу",
                             reply_markup=admin_button())
        else:
            bot.send_message(call.from_user.id,
                             "Администратор уже назначен. Хотите занять его роль? \n",
                             reply_markup=yes_no_admin_reg_cash())

    if call.data == 'yes_reg_admin_cash':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        reg = Work_in_db.take_admin_id()
        admins = []
        for num_reg in reg:
            if num_reg[-2] == '1':
                admins.append(num_reg)
        if not admins:
            Work_in_db.add_reg_for_cash_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "Теперь вы администратор по заявкам на перевод денег\n",
                             reply_markup=admin_button())
        else:
            bot.send_message(Work_in_db.take_first_admin_id(),
                             f"Вы больше не являетесь администратором по переводам!\n"
                             f"Новый администратор по переводам: @{Work_in_db.take_name_admin(call.from_user.id)}")
            Work_in_db.add_reg_for_cash_admin(admins[0][1], None)
            Work_in_db.add_reg_for_cash_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "Теперь вы администратор по заявкам на перевод денег\n",
                             reply_markup=admin_button())

    if call.data == 'admin_reg_for_contact':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if Work_in_db.exist_admin_reg_contacts() is False:
            Work_in_db.add_reg_for_contact_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "На данный момент на эту роль никто не назначен! Я назначаю вас. \n"
                             "Для смены роли попросите назначиться другому админу",
                             reply_markup=admin_button())
        else:
            bot.send_message(call.from_user.id,
                             "Администратор уже назначен. Хотите занять его роль? \n",
                             reply_markup=yes_no_admin_reg_contact())

    if call.data == 'yes_reg_admin_contact':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        reg = Work_in_db.take_admin_id()
        admins = []
        for num_reg in reg:
            if num_reg[-1] == '1':
                admins.append(num_reg)
        if not admins:
            Work_in_db.add_reg_for_contact_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "Теперь ваши данные указываются для контактов водителям\n",
                             reply_markup=admin_button())
        else:
            bot.send_message(Work_in_db.take_first_admin_id(),
                             f"Ваши данные больше не указываются как контактные!\n"
                             f"Новый администратор по контактам: @{Work_in_db.take_name_admin(call.from_user.id)}")
            Work_in_db.add_reg_for_contact_admin(admin[0][1], None)
            Work_in_db.add_reg_for_contact_admin(call.from_user.id, '1')
            bot.send_message(call.from_user.id,
                             "Теперь ваши данные указываются для контактов водителям\n",
                             reply_markup=admin_button())


def money_balance(message):
    enter_money = message.text
    money = []
    if enter_money == '0':
        bot.send_message(
            message.from_user.id,
            "Возвращаемся в меню!",
            reply_markup=room_for_driver())
    else:
        for num in enter_money:
            if num.isdigit() is True or num == "." or num == ",":
                money.append(num)
        full_money = ''
        for i in money:
            full_money += i
        Work_in_db.save_info_money(message.from_user.id, Work_in_db.exist_number_phone(message.from_user.id)[0][0],
                                   message.message_id, full_money, 5)
        bot.send_message(message.from_user.id,
                         "Запрос на перевод с безнала на баланс создан. Я вас уведомлю по рассмотрению заявки",
                         reply_markup=room_for_driver())
        if Work_in_db.take_user_name(message.from_user.id)[0][0] is None:
            admins = Work_in_db.take_admin_id()
            mess_admin = []
            for call_admin in admins:
                if call_admin[5] == '1':
                    mess_admin.append(call_admin)
            if not mess_admin:
                pass
            else:
                bot.send_message(
                    mess_admin[0][1],
                    f"Заявка на перевод денег на баланс!\n"
                    f"Номер телефона: +{Work_in_db.exist_number_phone(message.from_user.id)[0][0]}\n"
                    f"Просят перевести с безнала на баланс:\n"
                    f"{Work_in_db.take_info_money(message.from_user.id)[0][0]} рублей",
                    reply_markup=admin_money_balance())
        elif Work_in_db.take_user_name(message.from_user.id)[0][0] is not None:
            admin_info = Work_in_db.take_admin_id()
            mess_admin = []
            for call_admin in admin_info:
                if call_admin[5] == '1':
                    mess_admin.append(call_admin)
            if not mess_admin:
                pass
            else:
                bot.send_message(
                    mess_admin[0][1],
                    f"Заявка на перевод денег на баланс!\n"
                    f"Номер телефона: +{Work_in_db.exist_number_phone(message.from_user.id)[0][0]}\n"
                    f"Ссылка на телеграмм: @{Work_in_db.take_user_name(message.from_user.id)[0][0]}\n"
                    f"Просят перевести с безнала на баланс:\n"
                    f"{Work_in_db.take_info_money(message.from_user.id)[0][0]} рублей",
                    reply_markup=admin_money_balance())


def change_number_driver(message):
    phone = message.text
    number = []
    if phone == '0':
        bot.send_message(
            message.chat.id,
            "Регистрация отменена!",
            reply_markup=room_for_driver())
    else:
        for num in phone:
            if num.isdigit() is True:
                number.append(num)
        if len(number) != 12:
            bot.send_message(
                message.chat.id,
                "Ошибка в номере телефона! Попробуйте ещё раз")
            number.clear()
            bot.register_next_step_handler(message, change_number_driver)
        if len(number) != 0:
            full_number = ''
            for i in number:
                full_number += i
            url = requests.get(f'{settings.URL}{full_number}')
            if url.json()["status"] == "EXISTS":
                bot.send_message(
                    message.chat.id,
                    f"Смена номера не доступна, обратитесь к администратору: "
                    f"@{Work_in_db.take_first_admin_name()[0][0]}\n"
                    f"Или по телефону: +{Work_in_db.take_first_admin_num()[0][0]}",
                    reply_markup=room_for_driver())
            elif url.json()["status"] == "NOT_EXISTS":
                bot.send_message(
                    message.chat.id,
                    f"Запрос на смену номера отправлен!",
                    reply_markup=room_for_driver())
                admins = Work_in_db.take_admin_id()
                mess_admin = []
                for call_admin in admins:
                    if call_admin[4] == '1':
                        mess_admin.append(call_admin)
                bot.send_message(
                    mess_admin[0][1],
                    f"Запрос на смену номера телефона!\n"
                    f"Старый номер телефона: +{Work_in_db.exist_number_phone(message.from_user.id)[0][0]}\n"
                    f"Новый номер телефона: +{full_number}",
                    reply_markup=admin_change_num_driver_phone())
                Work_in_db.save_info_num(message.from_user.id,
                                         Work_in_db.exist_number_phone(message.from_user.id)[0][0],
                                         message.message_id, full_number, '10')
            elif url.json()['status'] == 'BLOCKED':
                bot.send_message(
                    message.chat.id,
                    f"Смена номера не доступна, обратитесь к администратору: @{Work_in_db.take_first_admin_name()}\n"
                    f"Или по телефону: +{Work_in_db.take_first_admin_num()}",
                    reply_markup=room_for_driver())
            # Work_in_db.add_number_phone(message.from_user.id, full_number)
            # bot.send_message(
            #     message.chat.id,
            #     "Номер успешно изменён",
            #     reply_markup=room_for_driver())


def change_number_admin(message):
    phone = message.text
    number = []
    if phone == '0':
        bot.send_message(
            message.chat.id,
            "Регистрация отменена!",
            reply_markup=admin_button())
    else:
        for num in phone:
            if num.isdigit() is True:
                number.append(num)
        if len(number) != 12:
            bot.send_message(
                message.chat.id,
                "Ошибка в номере телефона! Попробуйте ещё раз")
            number.clear()
            bot.register_next_step_handler(message, change_number_admin)
        if len(number) != 0:
            full_number = '+'
            for i in number:
                full_number += i
            Work_in_db.add_admin_phone(message.from_user.id, full_number)
            bot.send_message(
                message.chat.id,
                "Номер успешно изменён",
                reply_markup=admin_button())


def add_admin(message):
    new_adm = message.text
    if new_adm == '0':
        bot.send_message(
            message.chat.id,
            f"Регистрация отменена!",
            reply_markup=admin_button())
    else:
        Work_in_db.add_admin(new_adm)
        bot.send_message(
            message.chat.id,
            f"Администратор успешно добавлен!\n"
            f" \n"
            f"!!!Прошу обратить ваше внимание!!!\n"
            f"Для того, чтобы бот отправлял запросы о регистрации, новому администратору, "
            f"вам нужно передать ссылку на этого бота, попросить начать работу и ввести номер телефона.\n"
            f"Без этих действий бот не сможет взаимодействовать с новым администратором!",
            reply_markup=admin_button())


@bot.message_handler(commands=['admin'])
def admin(message):
    if Work_in_db.user_exists_admin(message.from_user.id) is True:
        if Work_in_db.admin_exists_name(message.from_user.id)[0][0] != message.from_user.username:
            Work_in_db.add_admin_user_name(message.from_user.username, message.from_user.id)
        bot.send_message(message.from_user.id, 'Добро пожаловать в панель администратора!')
        if Work_in_db.take_name_admin(message.from_user.id)[0][0] is None:
            bot.send_message(message.from_user.id, 'Для продолжения работы, пожалуйста, зайдите в'
                                                   ' настройки - изменить профиль - имя пользователя.\n '
                                                   'Мне он нужен для того, чтобы иметь ссылку на ващ ТГ!\n'
                                                   ' \n'
                                                   'По завершению снова используйте команду /admin')
        else:
            if Work_in_db.admin_exist_num(message.from_user.id)[0][0] is None:
                bot.send_message(
                    chat_id=message.chat.id,
                    text=f'Введите ваш номер телефона')
                bot.register_next_step_handler(message, enter_new_admin_number)
            else:
                bot.send_message(
                    message.chat.id,
                    "Меню дополнительных настроек",
                    reply_markup=admin_button())
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Вы не являетесь администратором!')


# while True:
#     try:
#         bot.polling(none_stop=True)
#
#     except Exception as e:
#         if "message to delete not found" in e or "host='api.telegram.org'" in e:
#             logger.error(e)
#             time.sleep(1)
#         else:
#             bot.send_message(-1001768253533, f'Произошла ошибка!\n'
#                                              f'Время совершения ошибки: {datetime.datetime.now()}\n'
#                                              f'Лог ошибки: {e}\n'
#                                              f'Перезапускаюсь!')
#             logger.error(e)
#             time.sleep(1)

if __name__ == '__main__':
    bot.polling(none_stop=True)
