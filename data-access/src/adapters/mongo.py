'''
This module is a MongoDB adapter for the data-access microservice.
'''
import certifi
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

from src.adapters.database import DatabaseAdapter
from src.etc.exceptions import DatabaseException

class MongoAdapter(DatabaseAdapter):
    '''
    MongoDB database adapter with which connection
    with a MongoDB database can be established.
    '''
    def __add_credentials_to_host(self):
        '''
        Method to format the MongoDB connection URI.
        '''
        self.host = f'mongodb+srv://{self.username}:{self.password}@{self.host}'

    def connect(self, database_name):
        '''
        Establishes a connection with the database and returns an object with
        which the database can be interacted with.
        :param database_name: Name of the default database.
        :return: client
        :rtype: MongoClient
        '''
        self.default_database = database_name
        self.__add_credentials_to_host()
        self.client = MongoClient(f'{self.host}/{database_name}', self.port, tlsCAFile=certifi.where())
        return self.client

    def insert(self, database_name, collection_name, data):
        '''
        Method to insert data into a table or collection
        :param database_name:
        :param collection_name:
        :param data:
        '''
        database = self.client[database_name]
        collection = database[collection_name]
        try:
            collection.insert_one(data)
            return {'response': 200}
        except DatabaseException:
            return {'response': 500}

    def find_by_oid(self, database_name, collection_name, oid=None):
        '''
        Method to read data from a table or colleection
        :param database_name:
        :param collection_name:
        :param oid:
        '''
        database = self.client[database_name]
        collection = database[collection_name]
        if oid is not None:
            try:
                return dumps(list(collection.find_one({"_id": ObjectId(oid)})))
            except DatabaseException as e:
                return {'response': 500, 'message': e}
        else:
            try:
                return dumps(list(collection.find()))
            except DatabaseException as e:
                return {'response': 500, 'message': e}
