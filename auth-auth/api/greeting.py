from flask import Blueprint

from operators.greeting import GreetingOperator

greeting_routes = Blueprint('greeting_routes', __name__)

@greeting_routes.route('/greet/<name>')
def greet(name):
    greeting_operator = GreetingOperator(name)
    return greeting_operator.greet()
