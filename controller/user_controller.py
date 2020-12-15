import json

from flask import Blueprint
from flask import jsonify, request
from repository.user_repository import UserRepository
from service.user_service import UserService
from controller.mapper import Mapper
from werkzeug.security import generate_password_hash
user_repo = UserRepository()
user_service = UserService(user_repo)


users = Blueprint('users',__name__)
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


@users.route('/users', methods=['GET'])
def get_users():
    user_id = request.args.get('userid')
    if user_id is None:
        # get all users
        return jsonify([Mapper.get_instance().user_to_json(user) for user in user_service.getAll()])
    else:
        # get one user
        user = user_service.getOne(user_id)
        return Mapper.get_instance().user_to_json(user)


@users.route('/users', methods=['POST'])
def save_user():
    user = Mapper.get_instance().json_to_user(request.json)
    user_service.send_password_email(user) # old, plain text password is used to send it as an email to the user
    user.set_password(generate_password_hash(user.get_password())) # method : "pbkdf2:sha256"
    user_service.add(user)
    return Mapper.get_instance().user_to_json(user)


@users.route('/users', methods=['PUT'])
def update_user():
    user = Mapper.get_instance().json_to_user(request.json)
    user_service.update(user)
    return Mapper.get_instance().user_to_json(user)


@users.route('/users', methods=['DELETE'])
def delete_users():
    user_id = request.args.get('userid')
    user_service.remove(user_id)
    return jsonify(success=True)