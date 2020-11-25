from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from domain import user
from controller.mapper import Mapper

from controller import user_controller
from controller import client_controller
from repository.client_repository import ClientRepository
from repository.department_repository import DepartmentRepository
from service.client_service import ClientService
from service.department_service import DepartmentService

app = Flask(__name__)
app.register_blueprint(user_controller.auth)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '123abc7891337'
app.config.from_object('database.database_config.Config')
db = SQLAlchemy(app)

# This will be moved in a separated file for client controller
client_repo = ClientRepository()
client_service = ClientService(client_repo)


@app.route('/clients', methods=['GET'])
def get_clients():
    client_id = request.args.get('clientid')
    if client_id is None:
        # get all clients
        return jsonify([Mapper.get_instance().client_to_json(client) for client in client_service.getAll()])
    else:
        # get one client
        client = client_service.getOne(client_id)
        return Mapper.get_instance().client_to_json(client)


@app.route('/clients', methods=['POST'])
def save_client():
    client = Mapper.get_instance().json_to_client(request.json)
    client_service.add(client)
    return Mapper.get_instance().client_to_json(client)


@app.route('/clients', methods=['PUT'])
def update_client():
    client = Mapper.get_instance().json_to_client(request.json)
    client_service.update(client)
    return Mapper.get_instance().client_to_json(client)


@app.route('/clients', methods=['DELETE'])
def delete_clients():
    client_id = request.args.get('clientid')
    client_service.remove(client_id)
    return jsonify(success=True)


# This will be moved in a separated file for department controller
department_repo = DepartmentRepository()
department_service = DepartmentService(department_repo)


@app.route('/departments', methods=['GET'])
def get_departments():
    department_id = request.args.get('departmentid')
    if department_id is None:
        # get all departments
        return jsonify(
            [Mapper.get_instance().department_to_json(department) for department in department_service.getAll()])
    else:
        # get one client
        department = department_service.getOne(department_id)
        return Mapper.get_instance().client_to_json(department)


@app.route('/departments', methods=['POST'])
def save_department():
    department = Mapper.get_instance().json_to_department(request.json)
    department_service.add(department)
    return Mapper.get_instance().department_to_json(department)


@app.route('/departments', methods=['PUT'])
def update_department():
    department = Mapper.get_instance().json_to_department(request.json)
    department_service.update(department)
    return Mapper.get_instance().department_to_json(department)


@app.route('/departments', methods=['DELETE'])
def delete_departments():
    department_id = request.args.get('departmentid')
    department_service.remove(department_id)
    return jsonify(success=True)


if __name__ == '__main__':
    app.run()
