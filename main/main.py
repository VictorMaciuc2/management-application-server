from flask import Flask
from flask_cors import CORS

from controller import UserController

app = Flask(__name__)
app.register_blueprint(UserController.auth)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '123abc7891337'
app.config.from_object('database.database_config.Config')


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/people')
def getNames():
    return {
        'people': ['Filip', 'Vlad']
    }
