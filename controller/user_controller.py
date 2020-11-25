from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
import json

from domain import user
from repository.user_repository import UserRepository
from service import user_service
from repository import user_repository
from flask_sqlalchemy import SQLAlchemy

from service.user_service import UserService

auth = Blueprint('auth', __name__)

userRepo = UserRepository()
userService = UserService(userRepo)


@auth.route('/login', methods=['POST'])
def login_post():
    from controller.mapper import Mapper

    user = userService.matchUserPassword(Mapper.get_instance().json_to_user(request.json))

    if user is None:
        return json.dumps(user)

    return Mapper.get_instance().user_to_json(user)
