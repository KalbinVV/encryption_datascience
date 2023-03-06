import json
import sqlite3

from Storage.DataStorage import DataStorage


class SqliteDataStorage(DataStorage):

    instance_ptr = None

    def __init__(self):
        try:
            self.__connection = sqlite3.connect('data.db')
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
            data_json json not null
        );
        '''

        cursor.execute(create_table_query)
        self.__connection.commit()

    # TODO: Add database
    def add_data(self, data: dict) -> None:
        cursor = self.__connection.cursor()

        # add_data_query = "insert into data(json) values(json('{json}')) returning id".format(json=data)

        # cursor.execute(add_data_query)

        # data_id = cursor.fetchone()['id']

        # self.__connection.commit()

        return 0
