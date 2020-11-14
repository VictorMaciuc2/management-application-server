from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask,Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy
from domain import User
from service import UserService
from repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '123abc7891337'
app.config.from_object('database.database_config.Config')
db=SQLAlchemy(app)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/people')
def getNames():
    return {
        'people': ['Filip','Vlad']
    }

@app.route('/login', methods=['POST'])
def login_post():
    email = request.json['email']
    password = request.json['password']

    userPosibil =User.User(None,None,email,password,None,None,None)
    userRepo = UserRepository.UserRepository
    service = UserService.UserService(userRepo)
    user = service.matchUserPassword(userPosibil)


    user1 = {'id':user.id,'email':user.email,'name':user.name,'password':user.password,'role':user.role,
             'seniority_level':user.seniority_level,'department_id':user.department_id}
    return user1



if __name__ == '__main__':
    app.run()

