'''
API Routes for the Data-Access microservice.
'''
import os
from flask.blueprints import Blueprint
from flask import request
from dotenv import load_dotenv

from src.adapters.mongo import MongoAdapter
from src.etc.config import ConfigHandler

load_dotenv()
config = ConfigHandler()

database_adapter = {
    'mongodb': MongoAdapter
}

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/<database>/<collection>', methods = ['GET', 'POST'])
def insert(database, collection):
    '''
    API Route to insert data into a database.
    '''
    db_adapter = database_adapter[config['database_type']](
        os.getenv('DATABASE_HOST'),
        os.getenv('DATABASE_PORT'),
        os.getenv('DATABASE_USER'),
        os.getenv('DATABASE_PASS')
    )
    db_adapter.connect(database)
    if request.method == 'GET':
        if request.args.get('oid') is not None:
            response = db_adapter.find_by_oid(database, collection, request.args.get('id'))
        else:
            print('No oid passed with request')
            response = db_adapter.find_by_oid(database, collection)
    elif request.method == 'POST':
        response = db_adapter.insert(database, collection, request.get_json())
    return response
