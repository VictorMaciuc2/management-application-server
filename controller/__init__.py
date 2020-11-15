from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy
from domain import User

from controller import UserController
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.register_blueprint(UserController.auth)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '123abc7891337'
app.config.from_object('database.database_config.Config')
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/people')
def getNames():
    return {
        'people': ['Filip', 'Vlad']
    }


if __name__ == '__main__':
    app.run()


