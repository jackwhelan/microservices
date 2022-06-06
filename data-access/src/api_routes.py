'''
API Routes for the Data-Access microservice.
'''
import os
from flask.blueprints import Blueprint
from flask import request

from src.adapters.mongo import MongoAdapter
from src.etc.config import ConfigHandler

config = ConfigHandler()

database_adapter = {
    'mongodb': MongoAdapter
}

db = database_adapter[config['database_type']](
    os.getenv('DATABASE_HOST'),
    os.getenv('DATABASE_PORT'),
    os.getenv('DATABASE_USER'),
    os.getenv('DATABASE_PASS')
)

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/<database>/<collection>', methods = ['GET', 'POST'])
def insert(database, collection):
    '''
    API Route to insert data into a database.
    '''
    db.connect(database)
    if request.method == 'GET':
        if request.args.get('id') is not None:
            return db.find_by_id(database, collection, request.args.get('id'))
        else:
            print('No id passed with request')
            return db.find_by_id(database, collection)
    elif request.method == 'POST':
        return db.insert(database, collection, request.form)
