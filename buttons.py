import settings
import telebot
from telebot import types

global files_park
files_park = {}


def menu_districts():
    keyboard = types.InlineKeyboardMarkup()
    my_flit = types.InlineKeyboardButton(text="Майфлит", callback_data='my_flit')
    drive = types.InlineKeyboardButton(text="Драйв", callback_data='drive')
    park = types.InlineKeyboardButton(text="Выбрать парк из списка", callback_data='park')
    back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
    keyboard.add(my_flit)
    keyboard.add(drive)
    keyboard.add(park)
    keyboard.add(back_rooms)
    return keyboard


def if_not_drive():
    keyboard = types.InlineKeyboardMarkup()
    reg_driver = types.InlineKeyboardButton(text="Войти водителем", callback_data='reg_driver')
    reg_park = types.InlineKeyboardButton(text="Войти партнёром", callback_data="reg_park")
    keyboard.add(reg_driver)
    keyboard.add(reg_park)
    return keyboard


def back_menu_rooms():
    keyboard = types.InlineKeyboardMarkup()
    back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
    keyboard.add(back_rooms)
    return keyboard


def districts1():
    keyboard = types.InlineKeyboardMarkup()
    central = types.InlineKeyboardButton(text="Центральный район", callback_data='central')
    soviet = types.InlineKeyboardButton(text="Советский район", callback_data='soviet')
    pervomai = types.InlineKeyboardButton(text="Первомайский район", callback_data='pervomai')
    up = types.InlineKeyboardButton(text="Вперёд", callback_data='up')
    down = types.InlineKeyboardButton(text="Вернуться в меню", callback_data='down')
    keyboard.add(central)
    keyboard.add(soviet)
    keyboard.add(pervomai)
    keyboard.add(down, up)
    return keyboard


def districts2():
    keyboard = types.InlineKeyboardMarkup()
    partiz = types.InlineKeyboardButton(text="Партизанский район", callback_data='partiz')
    zavod = types.InlineKeyboardButton(text="Заводской район", callback_data='zavod')
    lenin = types.InlineKeyboardButton(text="Ленинский район", callback_data='lenin')
    up = types.InlineKeyboardButton(text="Вперёд", callback_data='up')
    down = types.InlineKeyboardButton(text="Назад", callback_data='down')
    keyboard.add(partiz)
    keyboard.add(zavod)
    keyboard.add(lenin)
    keyboard.add(down, up)
    return keyboard


def districts3():
    keyboard = types.InlineKeyboardMarkup()
    october = types.InlineKeyboardButton(text="Октябрьский район", callback_data='october')
    moscow = types.InlineKeyboardButton(text="Московский район", callback_data='moscow')
    frunze = types.InlineKeyboardButton(text="Фрунзенский район", callback_data='frunze')
    up = types.InlineKeyboardButton(text="Вернуться в меню", callback_data='up')
    down = types.InlineKeyboardButton(text="Назад", callback_data='down')
    keyboard.add(october)
    keyboard.add(moscow)
    keyboard.add(frunze)
    keyboard.add(down, up)
    return keyboard


def enter_park_info(name_p=None,
                    unp_p=None,
                    num_p=None,
                    email_p=None,
                    address_p=None):
    keyboard = types.InlineKeyboardMarkup()
    name = types.InlineKeyboardButton(text="Имя", callback_data='name')
    unp = types.InlineKeyboardButton(text="УНП", callback_data='unp')
    num = types.InlineKeyboardButton(text="Номер", callback_data='num')
    email = types.InlineKeyboardButton(text="Мыло", callback_data='email')
    address = types.InlineKeyboardButton(text="Адрес", callback_data='address')
    next_reg = types.InlineKeyboardButton(text="Продолжить", callback_data='next_reg_driver')
    back_reg = types.InlineKeyboardButton(text="Изменить введённые данные", callback_data='back_reg')
    back_rooms = types.InlineKeyboardButton(text="Назад", callback_data='back_rooms')
    buttons_dict = {name: name_p, unp: unp_p, num: num_p, email: email_p, address: address_p}
    num_buttons = []
    for i in buttons_dict:
        if buttons_dict[i] is None:
            keyboard.add(i)
        else:
            num_buttons.append(i)
        if len(num_buttons) == 5:
            keyboard.add(next_reg)
            keyboard.add(back_reg)
    keyboard.add(back_rooms)
    return keyboard


class Texts:
    text_menu_park = '*"Смартдрайв" - парк на выбор*\n' \
                     ' \n' \
                     '\u2705 Комиссия ARMI 0%\n' \
                     '\u2705 Комиссия партнёра до 15%\n' \
                     '\u2705 Ежедневные выплаты\n' \
                     '\u2705 Официальное трудоустройство\n' \
                     'Выберите район:'
    text_all_tariff = 'У вас отсутствует подключение к парку.\n' \
                      'Мы можем предложить вам тарифы "Майфлит"(ИП) и "Драйв"(физ)\n ' \
                      ' \n' \
                      'Либо "Смартдрайв" - парк на выбор, ' \
                      'при подключении к парку комиссия арми 0%:\n'


class Buttons:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def back_menu(self, message_call):
        self.bot.clear_step_handler_by_chat_id(message_call.from_user.id)
        try:
            self.bot.edit_message_text(
                chat_id=message_call.from_user.id,
                message_id=message_call.message.message_id,
                text="Выберите нужный кабинет Armi\n",
                reply_markup=if_not_drive())
        except AttributeError:
            self.bot.edit_message_text(
                chat_id=message_call.from_user.id,
                message_id=message_call.message_id,
                text="Выберите нужный кабинет Armi\n",
                reply_markup=if_not_drive())

    def up(self, message_call, mes):
        try:
            if 'Советский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts2())
            elif 'Заводской район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts3())
            elif 'Московский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message.message_id,
                                           text=f'{Texts.text_all_tariff}',
                                           reply_markup=menu_districts())
        except AttributeError:
            if 'Советский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts2())
            elif 'Заводской район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts3())
            elif 'Московский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message_id,
                                           text=f'{Texts.text_all_tariff}',
                                           reply_markup=menu_districts())

    def down(self, message_call, mes):
        try:
            if 'Советский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message.message_id,
                                           text=f'{Texts.text_all_tariff}',
                                           reply_markup=menu_districts())
            elif 'Заводской район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts1())
            elif 'Московский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.message.chat.id,
                                           message_id=message_call.message.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts2())
        except AttributeError:
            if 'Советский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.chat.id,
                                           message_id=message_call.message_id,
                                           text=f'{Texts.text_all_tariff}',
                                           reply_markup=menu_districts())
            elif 'Заводской район' in mes:
                self.bot.edit_message_text(chat_id=message_call.chat.id,
                                           message_id=message_call.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts1())
            elif 'Московский район' in mes:
                self.bot.edit_message_text(chat_id=message_call.chat.id,
                                           message_id=message_call.message_id,
                                           text=f'{Texts.text_menu_park}',
                                           parse_mode='Markdown',
                                           reply_markup=districts2())

