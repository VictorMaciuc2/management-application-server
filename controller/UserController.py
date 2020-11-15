from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from service import UserService
from repository import UserRepository
from flask_sqlalchemy import SQLAlchemy
from domain import User


auth = Blueprint('auth',__name__)

userRepo = UserRepository.UserRepository()
userService = UserService.UserService(userRepo)


@auth.route('/login', methods=['POST'])
def login_post():
    content = request.json
    email = request.json['email']
    password = request.json['password']

    userPosibil = User.User(None, None, email, password, None, None, None)
    user = userService.matchUserPassword(userPosibil)

    user1 = {'id': user.id, 'email': user.email, 'name': user.name, 'password': user.password, 'role': user.role,
             'seniority_level': user.seniority_level, 'department_id': user.department_id}
    return user1



