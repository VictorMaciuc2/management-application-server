import json

from flask import Blueprint, Response
from flask import jsonify, request

from controller.helpers.authorize import auth_required
from controller.helpers.mapper import Mapper
from repository.department_repository import DepartmentRepository
from repository.user_repository import UserRepository
from service.department_service import DepartmentService
from service.user_service import UserService
from werkzeug.security import generate_password_hash
user_repo = UserRepository()
user_service = UserService(user_repo)


users = Blueprint('users',__name__)
auth = Blueprint('auth', __name__)

userRepo = UserRepository()
userService = UserService(userRepo)
department_repo = DepartmentRepository()
department_service = DepartmentService(department_repo)

@auth.route('/login', methods=['POST'])
def login_post():
    user = userService.matchUserPassword(request.json['email'], request.json['password'])
    if user is None:
        return json.dumps(user)

    jsonUser = Mapper.get_instance().user_to_json(user, department_service.getOne(user.department_id))
    jsonUser['jwtToken'] = userService.generate_token(user.id)
    return jsonify(jsonUser)


@users.route('/users', methods=['GET'])
@auth_required
def get_users():
    user_id = request.args.get('userid')
    if user_id is None:
        # get all users
        users = []
        for user in user_service.getAll():
            users.append(Mapper.get_instance().user_to_json(user, department_service.getOne(user.department_id)))
        return jsonify(users)
    else:
        # get one user
        user = user_service.getOne(user_id)
        return Mapper.get_instance().user_to_json(user, department_service.getOne(user.department_id))


@users.route('/users', methods=['POST'])
@auth_required
def save_user():
    user = Mapper.get_instance().json_to_user(request.json)
    try:
        user_service.send_password_email(user) # old, plain text password is used to send it as an email to the user
        user.set_password(generate_password_hash(user.get_password())) # method : "pbkdf2:sha256"
        user_service.add(user)
        user.set_department(department_service.getOne(user.department_id))
    except ValueError as err:
        return Response(err, 400)
    return Mapper.get_instance().user_to_json(user)


@users.route('/users', methods=['PUT'])
@auth_required
def update_user():
    user = Mapper.get_instance().json_to_user(request.json)
    try:
        user_service.update(user)
        user.set_department(department_service.getOne(user.department_id))
    except ValueError as err:
        return Response(err, 400)
    return Mapper.get_instance().user_to_json(user)


@users.route('/users', methods=['DELETE'])
@auth_required
def delete_users():
    user_id = request.args.get('userid')
    try:
        user_service.remove(user_id)
    except ValueError as err:
        return Response(err, 400)
    return jsonify(success=True)