'''
API Routes for the Data-Access microservice.
'''
import logging
import os
from flask.blueprints import Blueprint
from flask import request
from dotenv import load_dotenv

from src.adapters.mongo import MongoAdapter
from src.crud import create, read, update, delete
from src.etc.config import ConfigHandler

load_dotenv()
config = ConfigHandler()

database_adapter = {
    'mongodb': MongoAdapter
}

database_operation = {
    'POST': create,
    'GET': read,
    'PATCH': update,
    'DELETE': delete
}

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/<database>/<collection>', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
def db_interaction(database, collection):
    '''
    API Route to handle basic CRUD.
    '''
    db_adapter = database_adapter[config['database_type']](
        os.getenv('DATABASE_HOST'),
        os.getenv('DATABASE_PORT'),
        os.getenv('DATABASE_USER'),
        os.getenv('DATABASE_PASS')
    )
    response = database_operation[request.method](
        db_adapter,
        database,
        collection,
        request
    )
    return response
