from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from domain import user

from controller import user_controller
from controller import client_controller
from repository.client_repository import ClientRepository
from service.client_service import ClientService

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


if __name__ == '__main__':
    app.run()


