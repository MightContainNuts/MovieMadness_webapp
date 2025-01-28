# Description: all services related to the sql lite operations
# from application.app_factory import db
from typing import override
from logger import setup_logger

from data_manager import DataManagerInterface


class SQLiteDataManger(DataManagerInterface):
    def __init__(self):
        self.logger = setup_logger(__name__)
        self.logger.info("SQLite Data Manager created")

    def __str__(self):
        return "SQLite Data Manager"

    def __repr__(self):
        return "SQLite Data Manager"

    @override
    def get_all_users(self):
        pass

    @override
    def get_all_movies(self):
        pass

    @override
    def add_user(self):
        pass

    @override
    def update_movie(self):
        pass

    @override
    def delete_movie(self):
        pass
