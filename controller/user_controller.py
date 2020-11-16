from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
import json

from domain import user
from repository.user_repository import UserRepository
from service import user_service
from repository import user_repository
from flask_sqlalchemy import SQLAlchemy

from service.user_service import UserService

auth = Blueprint('auth',__name__)

userRepo = UserRepository()
userService = UserService(userRepo)


@auth.route('/login', methods=['POST'])
def login_post():
    content = request.json
    email = request.json['email']
    password = request.json['password']

    from domain.user import User
    user = User(email, password)
    addedUser = userService.matchUserPassword(user)

    if addedUser == None:
        return json.dumps(addedUser)

    jsonUser = {'id': addedUser.id, 'email': addedUser.email, 'name': addedUser.name, 'role': addedUser.role,
             'seniority_level': addedUser.seniority_level, 'department_id': addedUser.department_id}

    return jsonUser



