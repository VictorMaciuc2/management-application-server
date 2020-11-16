from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash

from repository.client_repository import ClientRepository
from repository.user_repository import UserRepository
from service import client_service
from repository import client_repository
from flask_sqlalchemy import SQLAlchemy

from service.client_service import ClientService
from service.user_service import UserService

auth = Blueprint('auth',__name__)

userRepo = ClientRepository()
userService = ClientService(userRepo)


@auth.route('/client', methods=['GET'])
def get_clients():
    return "Hy"