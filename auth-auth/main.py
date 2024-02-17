from flask import Flask

from api.greeting import greeting_routes

app = Flask(__name__)
app.register_blueprint(greeting_routes)

@app.route('/')
def default_route():
    return 'Default Route.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
