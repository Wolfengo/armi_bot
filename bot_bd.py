import sqlite3
import threading


class Armi_in_db:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def take_all(self):
        """Используется для проверки ожидающих регистрацию"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT * FROM `driver`")
            return result.fetchall()
        finally:
            self.lock.release()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id` FROM `driver` WHERE `user_id` = ?", (user_id,))
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def add_user(self, user_id, user_name):
        """Добавляем, юзера в базу"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("INSERT INTO `driver` (`user_id`, 'user_name') VALUES (?,?)", (user_id, user_name))
            return self.conn.commit()
        finally:
            self.lock.release()

    def add_admin(self, user_id):
        """Добавляем, юзера в базу"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("INSERT INTO `admin` (`user_id`) VALUES (?)", (user_id,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def add_admin_user_name(self, name, user_id):
        """Меняем имя аккаунта телеги админа"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE admin SET user_name = ? WHERE user_id = ?", (name, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def user_exists_name(self, user_id):
        """Проверяем, есть ли имя аккаунта в базе"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_id` FROM `driver` WHERE `user_name` = ?", (user_id,))
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def admin_exists_name(self, user_id):
        """Проверяем, есть ли имя аккаунта админа в базе"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_name` FROM `admin` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def change_user_name(self, name, user_id):
        """Меняем имя аккаунта телеги юзера"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET user_name = ? WHERE user_id = ?", (name, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def exist_number_phone(self, user_id):
        """Проверяем, записан ли номер телефона"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT number_phone FROM driver WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_number_phone(self, user_id, user_phone):
        """Добавляем, номер телефона"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET number_phone = ? WHERE user_id = ?", (user_phone, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_model_car(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT model_car FROM driver WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_model_car(self, user_id, model_car):
        """Добавляем, номер телефона"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET model_car = ? WHERE user_id = ?", (model_car, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_name_car(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT name_car FROM driver WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_name_car(self, user_id, name_car):
        """Добавляем, номер телефона"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET name_car = ? WHERE user_id = ?", (name_car, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_num_car(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT num_car FROM driver WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_num_car(self, user_id, num_car):
        """Добавляем, номер телефона"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET num_car = ? WHERE user_id = ?", (num_car, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_name_driver(self, user_id):
        """Берём имя водителя из базы данных"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT name_driver FROM driver WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def take_user_name(self, user_id):
        """Берём имя телеги водителя из базы данных"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT user_name FROM driver WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_name_driver(self, user_id, name_driver):
        """Добавляем имя водителя"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET name_driver = ? WHERE user_id = ?", (name_driver, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def user_exists_auto(self, user_id):
        """Проверяем, есть ли документ на авто в базе"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `car_doc1` FROM `driver` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_car_doc(self, user_id, car_doc):
        """Добавляем id фото документа с номером авто"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET car_doc1 = ? WHERE user_id = ?", (car_doc, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def del_doc(self, user_id, null=None):
        """Удаляем фотографии водителя, чтобы попросить загрузить их снова"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE `driver` SET 'car_doc1' = ? WHERE user_id = ?", (null, user_id,))
            self.cursor.execute("UPDATE `driver` SET 'driver_license_1' = ? WHERE user_id = ?", (null, user_id,))
            self.cursor.execute("UPDATE `driver` SET 'driver_license_2' = ? WHERE user_id = ?", (null, user_id,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def del_doc_car(self, user_id, null=None):
        """Удаляем фотографи документа на авто, чтобы попросить загрузить их снова"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE `driver` SET 'car_doc1' = ? WHERE user_id = ?", (null, user_id,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def del_doc_driver(self, user_id, null=None):
        """Удаляем фотографии поав, чтобы попросить загрузить их снова"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE `driver` SET 'driver_license_1' = ? WHERE user_id = ?", (null, user_id,))
            self.cursor.execute("UPDATE `driver` SET 'driver_license_2' = ? WHERE user_id = ?", (null, user_id,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_first_admin_num(self,):
        """Достаём номер первого админа из базы"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_number` FROM `admin` WHERE `reg_for_contact` = '1'")
            return result.fetchall()
        finally:
            self.lock.release()

    def take_admin_num(self, user_id):
        """Достаём номер первого админа из базы"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_number` FROM `admin` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def take_admin_id(self,):
        """Достаём номер первого админа из базы"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT * FROM `admin`")
            return result.fetchall()
        finally:
            self.lock.release()

    def take_first_admin_name(self,):
        """Достаём юзернейм телеги первого админа"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_name` FROM `admin` WHERE `reg_for_contact` = '1'",)
            return result.fetchall()
        finally:
            self.lock.release()

    def take_first_admin_id(self,):
        """Достаём юзернейм телеги первого админа"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_id` FROM `admin` WHERE `reg_for_contact` = '1'",)
            return result.fetchall()
        finally:
            self.lock.release()

    def take_admin_name(self, user_id):
        """Достаём юзернейм телеги первого админа"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_name` FROM `admin` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def user_exists_drive1(self, user_id):
        """Проверяем, есть ли лицевая сторона прав"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `driver_license_1` FROM `driver` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_armi_driver(self, user_id, zero_or_one):
        """Используется при одобрении заявки 'помечаем' водителя как зарегистрированного"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET registration = ? WHERE user_id = ?", (zero_or_one, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def add_drive_doc1(self, user_id, car_doc):
        """Добавляем id фото прав с лицевой стороны"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET driver_license_1 = ? WHERE user_id = ?", (car_doc, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def user_exists_drive2(self, user_id):
        """Проверяем, есть ли обратная сторона прав"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `driver_license_2` FROM `driver` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_drive_doc2(self, user_id, car_doc):
        """Добавляем id фото прав с обратной стороны"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET driver_license_2 = ? WHERE user_id = ?", (car_doc, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def user_exists_register(self, user_id):
        """Проверяем номер регистра для работы"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `registration` FROM `driver` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_user_register(self, user_id, register):
        """Добавляем номер регистра для работы"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE driver SET registration = ? WHERE user_id = ?", (register, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def user_exists_admin(self, user_id):
        """Проверяем, есть ли админ в базе"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id` FROM `admin` WHERE `user_id` = ?", (user_id,))
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def admin_exist_num(self, user_id):
        """Достаём номер админа"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `user_number` FROM `admin` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_admin_phone(self, user_id, user_phone):
        """Добавляем/меняем, номер телефона"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE admin SET user_number = ? WHERE user_id = ?", (user_phone, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def del_mess(self, id_mess, chat_id):
        """Добавляем, юзера в базу"""
        try:
            self.lock.acquire(True)
            self.cursor.execute("INSERT INTO `delete_mess` (`id_mess`, `chat_id`) VALUES (?, ?)", (id_mess, chat_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_del_mess(self, chat_id):
        """Достаём номер админа"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id_mess` FROM `delete_mess` WHERE `chat_id` = ?", (chat_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def clear_del_mess(self, id_mess):
        try:
            self.lock.acquire(True)
            self.cursor.execute("DELETE FROM `delete_mess` WHERE id_mess = ?", (id_mess,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def save_info(self, user_id, num_user, id_mess, reg):
        try:
            self.lock.acquire(True)
            self.cursor.execute("INSERT INTO `info` (`user_id`, 'num_user', 'id_mess', 'reg') VALUES (?,?,?,?)",
                                (user_id, num_user, id_mess, reg))
            return self.conn.commit()
        finally:
            self.lock.release()

    def save_info_num(self, user_id, num_user, id_mess, money, reg):
        try:
            self.lock.acquire(True)
            self.cursor.execute("INSERT INTO `info` (`user_id`, 'num_user', 'id_mess', 'reg', 'text') VALUES (?,?,?,?,?)",
                                (user_id, num_user, id_mess, reg, money))
            return self.conn.commit()
        finally:
            self.lock.release()

    def save_info_money(self, user_id, num_user, id_mess, money, reg):
        try:
            self.lock.acquire(True)
            self.cursor.execute("INSERT INTO `info` (`user_id`, 'num_user', 'id_mess', 'money', 'reg') VALUES (?,?,?,?,?)",
                                (user_id, num_user, id_mess, money, reg))
            return self.conn.commit()
        finally:
            self.lock.release()

    def exists_save_info(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id_mess` FROM `info` WHERE `user_id` = ?", (user_id,))
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def take_info_mess_id(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id_mess` FROM `info` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def new_info(self, user_id, num_user, id_mess):
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE info SET id_mess = ? WHERE user_id = ?", (id_mess, user_id))
            self.cursor.execute("UPDATE info SET num_user = ? WHERE user_id = ?", (num_user, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_user_id_info(self, id_mess):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT user_id FROM info WHERE id_mess = ?", (id_mess,))
            return result.fetchall()
        finally:
            self.lock.release()

    def take_user_num_info(self, id_mess):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT text FROM info WHERE id_mess = ?", (id_mess,))
            return result.fetchall()
        finally:
            self.lock.release()

    def delete_all_driver(self, user_id):
        try:
            self.lock.acquire(True)
            self.cursor.execute("DELETE FROM driver WHERE user_id = ?", (user_id,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def delete_info(self, user_id):
        try:
            self.lock.acquire(True)
            self.cursor.execute("DELETE FROM info WHERE user_id = ?", (user_id,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def delete_info_money(self, id_mess,):
        try:
            self.lock.acquire(True)
            self.cursor.execute("DELETE FROM info WHERE id_mess = ?", (id_mess,))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_info_reg(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `reg` FROM `info` WHERE `user_id` = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def take_all_info(self,):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT * FROM info",)
            return result.fetchall()
        finally:
            self.lock.release()

    def take_all_info_id(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT * FROM info WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def take_info_money(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT money FROM info WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def take_name_admin(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT user_name FROM admin WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def add_reg_for_docks_admin(self, user_id, reg_for_docks):
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE admin SET reg_for_docks = ? WHERE user_id = ?", (reg_for_docks, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def add_reg_for_cash_admin(self, user_id, reg_for_cash):
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE admin SET reg_for_cash = ? WHERE user_id = ?", (reg_for_cash, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def add_reg_for_contact_admin(self, user_id, reg_for_contact):
        try:
            self.lock.acquire(True)
            self.cursor.execute("UPDATE admin SET reg_for_contact = ? WHERE user_id = ?", (reg_for_contact, user_id))
            return self.conn.commit()
        finally:
            self.lock.release()

    def exist_admin_reg_docks(self,):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id` FROM `admin` WHERE `reg_for_docks` = '1'")
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def exist_admin_reg_cash(self,):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id` FROM `admin` WHERE `reg_for_cash` = '1'")
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def exist_admin_reg_contacts(self,):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id` FROM `admin` WHERE `reg_for_contact` = '1'")
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def take_admin_reg_all(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT * FROM admin WHERE user_id = ?", (user_id,))
            return result.fetchall()
        finally:
            self.lock.release()

    def exist_new_num_driver_user(self, user_id):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `text` FROM `info` WHERE `user_id` = ?", (user_id,))
            total = bool(len(result.fetchall()))
            if total is True:
                reg = 0
                info = self.cursor.execute("SELECT * FROM info WHERE user_id = ?", (user_id,))
                all_info = info.fetchall()
                for take_info in all_info:
                    if take_info[-3] == '10':
                        reg += 1
                        if reg == 1:
                            return True
                        if reg == 0:
                            return False
            else:
                return False
        finally:
            self.lock.release()
