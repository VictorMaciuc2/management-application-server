from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from controller import user_controller
from controller import client_controller
from controller import department_controller

app = Flask(__name__)
app.register_blueprint(user_controller.auth)
app.register_blueprint(department_controller.deps)
app.register_blueprint(client_controller.clients)
app.register_blueprint(user_controller.users)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '123abc7891337'
app.config.from_object('database.database_config.Config')
db = SQLAlchemy(app)

if __name__ == '__main__':

    from service.user_service import UserService
    from repository.user_repository import UserRepository
    from domain.user import User
    repo=UserRepository()
    service = UserService(repo)
    user = User(1,"nume","email","pass","rol","","")
    service.send_password_email(user)
    #app.run()
