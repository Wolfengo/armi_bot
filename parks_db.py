import sqlite3
import threading


class Parks_in_db:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()

    def park_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id` FROM `park_info` WHERE `id_park_tele` = ?", (user_id,))
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def park_num_exists(self, num_park):
        """Проверяем, есть ли номер телефона"""
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT `id` FROM `park_info` WHERE `num_park` = ?", (num_park,))
            return bool(len(result.fetchall()))
        finally:
            self.lock.release()

    def add_park_in_base(self, id_park, info_park):
        """Добавляем, id теглеги парка"""
        try:
            self.lock.acquire(True)
            name_park = info_park['name_p']
            unp_park = info_park['unp_p']
            num_park = info_park['num_p']
            email = info_park['email_p']
            address = info_park['address_p']
            # self.cursor.execute("INSERT INTO `parks` (`id_park`) VALUES (?)", (id_park,))
            self.cursor.execute("INSERT INTO `park_info` ('id_park_tele',`name_park`, "
                                "'YNP_park', 'num_park', 'email', 'address') VALUES (?,?,?,?,?,?)",
                                (id_park, name_park, unp_park, num_park, email, address))
            return self.conn.commit()
        finally:
            self.lock.release()

    def take_park_info(self, id_park):
        try:
            self.lock.acquire(True)
            result = self.cursor.execute("SELECT * FROM `park_info` WHERE id_park_tele = ?", (id_park,))
            return result.fetchall()
        finally:
            self.lock.release()

    def test(self,):
        self.cursor.execute("DELETE FROM park_info WHERE name_park= 'Васькин ООО'")
        return self.conn.commit()
