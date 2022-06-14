'''
This module is a MongoDB adapter for the data-access microservice.
'''
import certifi
from pymongo import MongoClient
from bson.objectid import ObjectId

from src.adapters.database import DatabaseAdapter

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
            return {
                'status_code': 200,
                'message': 'Inserted document into DB.'
            }, 200
        except Exception as err:
            return {
                'status_code': 500,
                'message': 'Failed to insert document into DB.',
                'exception': str(err)
            }, 500

    def find_by_oid(self, database_name, collection_name, oid=None):
        '''
        Method to read data from a table or collection
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
                return {
                    'response': document,
                    'status_code': 200
                }, 200
            except TypeError as err:
                return {
                    'response': document,
                    'status_code': 404, 'message': 'Could not find requested document.',
                    'exception': str(err)
                }, 404
            except Exception as err:
                return {
                    'response': document,
                    'status_code': 500,
                    'exception': str(err)
                }, 500
        else:
            try:
                documents = list(collection.find())
                for document in documents:
                    document['_id'] = str(document['_id'])
                return {
                    'response': documents,
                    'status_code': 200
                }, 200
            except Exception as err:
                return {
                    'response': document,
                    'status_code': 500,
                    'exception': str(err)
                }, 500

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
        try:
            updated_document = collection.find_one_and_update({ "_id": ObjectId(oid) }, { "$set": data })
            updated_document['_id'] = str(updated_document['_id'])
            return {
                'response': updated_document,
                'status_code': 200
            }, 200
        except TypeError as err:
            return {
                'status_code': 404,
                'message': 'Could not find document matching requested OID.',
                'exception': str(err)
            }, 404
        except Exception as err:
            return {
                'status_code': 500,
                'message': 'Could not fetch document matching requested OID. Check Data-Access service logs.',
                'exception': str(err)
            }, 500

    def delete(self, database_name, collection_name, oid):
        '''
        Method to find a document by id and delete it.
        :param database_name:
        :param table_name:
        :param oid:
        :param data:
        '''
        database = self.client[database_name]
        collection = database[collection_name]
        try:
            collection.delete_one({ "_id": ObjectId(oid) })
            return {
                'response': 200
            }, 200
        except Exception:
            return {
                'response': 500
            }, 500
