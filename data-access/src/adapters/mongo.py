'''
This module is a MongoDB adapter for the data-access microservice.
'''
import certifi
from pymongo import MongoClient
from bson.objectid import ObjectId

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
                document = collection.find_one({"_id": ObjectId(oid)})
                document['_id'] = str(document['_id'])
                return document
            except DatabaseException as err:
                return {'response': 500, 'message': err}
        else:
            try:
                return collection.find()
            except DatabaseException as err:
                return {'response': 500, 'message': err}

    def update(self, database_name, collection_name, oid, data):
        '''
        Method to find a document by id and update it.
        :param database_name:
        :param collection_name:
        :param oid:
        :param data:
        '''
        database = self.client[database_name]
        collection = database[collection_name]
        updated_document = collection.find_one_and_update({ "_id": ObjectId(oid) }, { "$set": data })
        updated_document['_id'] = str(updated_document['_id'])
        return updated_document
