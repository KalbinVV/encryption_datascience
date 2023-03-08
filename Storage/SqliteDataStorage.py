import datetime
import json
import os.path
import sqlite3

from Storage.DataStorage import DataStorage


class SqliteDataStorage(DataStorage):

    instance_ptr = None
    DIR_PATH = './data/'

    def __init__(self):
        try:
            self.__connection = sqlite3.connect('data.db', check_same_thread=False)
            self.init_table()
        except sqlite3.Error as e:
            print(e)

    @classmethod
    def instance(cls):
        if cls.instance_ptr:
            return cls.instance_ptr
        else:
            cls.instance_ptr = SqliteDataStorage()

            return cls.instance_ptr

    def init_table(self) -> None:
        cursor = self.__connection.cursor()

        create_table_query = '''
        create table if not exists data (
            id integer primary key,
            path text not null
        );
        '''

        cursor.execute(create_table_query)
        self.__connection.commit()

    def add_data(self, data: dict) -> None:
        dir_path = SqliteDataStorage.DIR_PATH
        file_name = str(datetime.datetime.now())

        file_path = dir_path + file_name

        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

        with open(file_path, 'w') as file:
            file.write(json.dumps(data))

        cursor = self.__connection.cursor()

        add_data_query = f'insert into data(path) values ("{file_path}")'
        cursor.execute(add_data_query)

        get_id_query = f'select id from data where path="{file_path}"'
        cursor.execute(get_id_query)
        data_id = cursor.fetchone()[0]

        self.__connection.commit()

        return data_id

    def get_data(self, data_id: int) -> dict:
        cursor = self.__connection.cursor()

        get_data_query = f'select path from data where id="{data_id}"'
        cursor.execute(get_data_query)
        file_path = cursor.fetchone()[0]

        self.__connection.commit()

        data = None

        with open(file_path, 'r') as file:
            data = json.load(file)

        return data
