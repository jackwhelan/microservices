'''
API Routes for the Data-Access microservice.
'''
from flask.blueprints import Blueprint

from src.use_cases.generate_greeting import greet_person

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/name/<name>')
def greet_by_name(name):
    '''
    Test function to lay down some boilerplate architecture.
    '''
    return greet_person(name)
