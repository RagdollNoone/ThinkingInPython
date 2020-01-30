import sqlite3
import os
import threading

OUTPUT_ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = "borg"


class DataBase(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.filename = os.path.join(OUTPUT_ROOT, OUTPUT_FILE)
        self._db = sqlite3.connect(self.filename)
        self._db.row_factory = sqlite3.Row
        self.cursor = self._db.cursor()
        return

    def execute(self, sql, *params):
        return self.cursor.execute(sql, params)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def last_row_id(self):
        return self.cursor.lastrowid

    def commit(self):
        self._db.commit()

    def close(self):
        self.commit()
        self._db.close()


db = DataBase()


def get_db_filename():
    db.filename


def execute(command):
    db.execute(command)


def commit():
    db.commit()


def close():
    db.close()


class AddThread(threading.Thread):
    def __init__(self, name, index):
        threading.Thread.__init__(self)
        self.name = name
        self.index = index

    def run(self):
        command = "INSERT INTO USER VALUES (" + str(self.index) + ", 'Dendy', 29);"
        print(self.name + " " + command)
        execute(command)
        commit()
        close()

    pass


def main():
    for i in range(1, 1):
        thread = AddThread("Thread-" + str(i), i)
        thread.start()

    pass


if __name__ == '__main__':
    main()

