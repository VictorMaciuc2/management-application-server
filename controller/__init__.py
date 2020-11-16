from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from domain import user

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
    if client_id == None:
        # get all clients
        jsonClients = []
        for client in client_service.getAll():
            jsonClients.append({'id': client.id, 'name': client.name, 'description': client.description})
        return jsonify(jsonClients)
    else:
        client = client_service.getOne(client_id)
        return {'id': client.id, 'name': client.name, 'description': client.description}

@app.route('/clients', methods=['POST'])
def post_clients():
    from domain.client import Client
    client_id = None
    if 'id' in request.json:
        client_id = request.json['id']

    client = Client(client_id, request.json['name'], request.json['description'])
    if client.id == None:
        # save client
        client_service.add(client)
    else:
        # update client
        client_service.update(client)

    return jsonify({'id': client.id, 'name': client.name, 'description': client.description})

@app.route('/clients', methods=['DELETE'])
def delete_clients():
    from domain.client import Client
    client_id = request.args.get('clientid')
    client_service.remove(client_id)
    return jsonify(success=True)

# This will be moved in a separated file for department controller
department_repo = DepartmentRepository()
department_service = DepartmentService(department_repo)

@app.route('/departments', methods=['GET'])
def get_departments():
    department_id = request.args.get('departmentid')
    if department_id == None:
        # get all departments
        jsondepartments = []
        for department in department_service.getAll():
            jsondepartments.append({'id': department.id, 'name': department.name, 'description': department.description})
        return jsonify(jsondepartments)
    else:
        department = department_service.getOne(department_id)
        return {'id': department.id, 'name': department.name, 'description': department.description}

@app.route('/departments', methods=['POST'])
def post_departments():
    from domain.department import Department
    department_id = None
    if 'id' in request.json:
        department_id = request.json['id']

    department = Department(department_id, request.json['name'], request.json['description'])
    if department.id == None:
        # save department
        department_service.add(department)
    else:
        # update department
        department_service.update(department)

    return jsonify({'id': department.id, 'name': department.name, 'description': department.description})

@app.route('/departments', methods=['DELETE'])
def delete_departments():
    from domain.department import Department
    department_id = request.args.get('departmentid')
    department_service.remove(department_id)
    return jsonify(success=True)


if __name__ == '__main__':
    app.run()


