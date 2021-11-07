from flask import Flask
from src.adapters.api_routes import api_routes

app = Flask(__name__)

@app.route("/")
def default_route():
    return "Default Route"

app.register_blueprint(api_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0')