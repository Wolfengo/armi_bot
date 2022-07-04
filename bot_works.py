import telebot
import settings
import main_bot
import buttons
from parks_db import Parks_in_db
from bot_bd import Armi_in_db

Work_in_db = Armi_in_db(settings.folder())
Parks = Parks_in_db(settings.folder())
bot = telebot.TeleBot(settings.test())
Blocks = buttons.Buttons(settings.test())
Buttons = buttons


def enter_num(message):
    phone = message.text
    number = []
    for num in phone:
        if num.isdigit() is True:
            number.append(num)
    if len(number) == 1 and number[0] == '0':
        return True
    if len(number) != 12:
        return False
    if len(number) != 0:
        full_number = ''
        for i in number:
            full_number += i
        return full_number


def take_info_park(message, call_data):
    text = message.text
    if call_data == 'name':
        buttons.files_park[message.from_user.id]['name_p'] = text
        create_info(message)
    elif call_data == 'unp':
        buttons.files_park[message.from_user.id]['unp_p'] = text
        create_info(message)
    elif call_data == 'num':
        buttons.files_park[message.from_user.id]['num_p'] = text
        create_info(message)
    elif call_data == 'email':
        buttons.files_park[message.from_user.id]['email_p'] = text
        create_info(message)
    elif call_data == 'address':
        buttons.files_park[message.from_user.id]['address_p'] = text
        create_info(message)


def create_info(message):
    num_buttons = []
    for i in buttons.files_park[message.from_user.id]:
        if buttons.files_park[message.from_user.id][i] is not None:
            num_buttons.append(i)
    if len(num_buttons) != 5:
        bot.send_message(message.from_user.id,
                         f"Выберите что будете заполнять",
                         reply_markup=buttons.enter_park_info
                         (name_p=buttons.files_park[message.from_user.id]['name_p'],
                          unp_p=buttons.files_park[message.from_user.id]['unp_p'],
                          num_p=buttons.files_park[message.from_user.id]['num_p'],
                          email_p=buttons.files_park[message.from_user.id]['email_p'],
                          address_p=buttons.files_park[message.from_user.id]['address_p']))
    else:
        bot.send_message(message.from_user.id,
                         f"Проверим введённые данные:\n"
                         f"Ваш парк: {buttons.files_park[message.from_user.id]['name_p']}\n"
                         f"Ваш УНП: {buttons.files_park[message.from_user.id]['unp_p']}\n"
                         f"Ваш номер: +{buttons.files_park[message.from_user.id]['num_p']}\n"
                         f"Ваш email: {buttons.files_park[message.from_user.id]['email_p']}\n"
                         f"Ваш адрес: {buttons.files_park[message.from_user.id]['address_p']}\n",
                         reply_markup=buttons.enter_park_info
                         (name_p=buttons.files_park[message.from_user.id]['name_p'],
                          unp_p=buttons.files_park[message.from_user.id]['unp_p'],
                          num_p=buttons.files_park[message.from_user.id]['num_p'],
                          email_p=buttons.files_park[message.from_user.id]['email_p'],
                          address_p=buttons.files_park[message.from_user.id]['address_p']))
