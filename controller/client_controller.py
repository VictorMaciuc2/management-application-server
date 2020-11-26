#Here will move client methods
from flask import Blueprint
from flask import jsonify, request
from repository.client_repository import ClientRepository
from service.client_service import ClientService
from controller.mapper import Mapper

client_repo = ClientRepository()
client_service = ClientService(client_repo)


clients = Blueprint('clients',__name__)

@clients.route('/clients', methods=['GET'])
def get_clients():
    client_id = request.args.get('clientid')
    if client_id is None:
        # get all clients
        return jsonify([Mapper.get_instance().client_to_json(client) for client in client_service.getAll()])
    else:
        # get one client
        client = client_service.getOne(client_id)
        return Mapper.get_instance().client_to_json(client)


@clients.route('/clients', methods=['POST'])
def save_client():
    client = Mapper.get_instance().json_to_client(request.json)
    client_service.add(client)
    return Mapper.get_instance().client_to_json(client)


@clients.route('/clients', methods=['PUT'])
def update_client():
    client = Mapper.get_instance().json_to_client(request.json)
    client_service.update(client)
    return Mapper.get_instance().client_to_json(client)


@clients.route('/clients', methods=['DELETE'])
def delete_clients():
    client_id = request.args.get('clientid')
    client_service.remove(client_id)
    return jsonify(success=True)