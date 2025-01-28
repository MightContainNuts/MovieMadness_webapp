# Description: Database management services
from abc import ABC, abstractmethod


class DataManagerInterface(ABC):
    def __init__(self):
        pass

    def __str__(self):
        return "Data Manager Interface"

    def __repr__(self):
        return "Data Manager Interface"

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_all_movies(self):
        pass

    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def update_movie(self):
        pass

    @abstractmethod
    def delete_movie(self):
        pass
