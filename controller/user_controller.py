from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash

from domain import user
from service import user_service
from repository import user_repository
from flask_sqlalchemy import SQLAlchemy


auth = Blueprint('auth',__name__)

userRepo = user_repository.UserRepository()
userService = user_service.UserService(userRepo)


@auth.route('/login', methods=['POST'])
def login_post():
    content = request.json
    email = request.json['email']
    password = request.json['password']

    userPosibil = User(email, password)
    user = userService.matchUserPassword(userPosibil)

    user1 = {'id': user.id, 'email': user.email, 'name': user.name, 'password': user.password, 'role': user.role,
             'seniority_level': user.seniority_level, 'department_id': user.department_id}
    return user1



