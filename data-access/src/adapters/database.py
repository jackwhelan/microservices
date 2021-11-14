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
        self.port = port
        self.username = username
        self.password = password

    @abstractmethod
    def connect(self, database_name):
        '''
        Establishes a connection with the database and returns an object with
        which the database can be interacted with.
        :param database_name: Name of the database to connect to.
        :return cursor: Object through which the database can be used.
        '''
