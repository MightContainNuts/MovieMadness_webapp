# Description: all services related to the sql lite operations
from app.__init__py import db
from typing import override

from data_manager import DataManagerInterface


class SQLiteDataManger(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db = db(db_file_name)

    @override
    def get_all_users(self):
        pass

    @override
    def get_all_movies(self):
        pass
