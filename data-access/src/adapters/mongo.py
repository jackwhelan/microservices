'''
This module is a MongoDB adapter for the data-access microservice.
'''
import certifi
from pymongo import MongoClient

from src.adapters.database import DatabaseAdapter

class MongoAdapter(DatabaseAdapter):
    '''
    MongoDB database adapter with which connection
    with a MongoDB database can be established.
    '''
    def __add_credentials_to_host(self):
        self.host = f'mongodb+srv://{self.username}:{self.password}@{self.host}'

    def connect(self, database_name):
        self.__add_credentials_to_host()
        return MongoClient(f'{self.host}/{database_name}', self.port, tlsCAFile=certifi.where())
