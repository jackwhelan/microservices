'''
This module is a generic database adapter that will
be inherited by more specific database adapters.
'''
from abc import ABC, abstractmethod

class DatabaseAdapter(ABC):
    '''
    Generic Database Adapter class used as an interface
    with which database connectivity can be established.
    '''
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password

    @abstractmethod
    def connect(self, database_name):
        '''
        Establishes a connection with the database and returns an object with
        which the database can be interacted with.
        :param database_name: Name of the database to connect to.
        :return: cursor
        '''
    
    @abstractmethod
    def insert(self, database_name, table_name, data):
        '''
        Method to insert data into a table or collection
        :param database_name:
        :param table_name:
        :param data:
        '''

    @abstractmethod
    def find_by_id(self, database_name, table_name, id):
        '''
        Method to find a document or row by id.
        :param database_name:
        :param table_name:
        :param id:
        '''
