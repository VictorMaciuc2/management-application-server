from flask import Blueprint, Response
from flask import jsonify, request

from controller.helpers.authorize import auth_required
from controller.helpers.mapper import Mapper
from repository.client_repository import ClientRepository
from service.client_service import ClientService

client_repo = ClientRepository()
client_service = ClientService(client_repo)


clients = Blueprint('clients',__name__)

@clients.route('/clients', methods=['GET'])
@auth_required
def get_clients():
    client_id = request.args.get('clientid')
    if client_id is None:
        # get all clients
        return jsonify([Mapper.get_instance().client_to_json(client) for client in client_service.getAll()])
    else:
        # get one client
        try:
            client = client_service.getOne(client_id)
        except ValueError as err:
            return Response(err, 400)
        return Mapper.get_instance().client_to_json(client)


@clients.route('/clients', methods=['POST'])
@auth_required
def save_client():
    client = Mapper.get_instance().json_to_client(request.json)
    try:
        client_service.add(client)
    except ValueError as err:
        return Response(err, 400)
    return Mapper.get_instance().client_to_json(client)


@clients.route('/clients', methods=['PUT'])
@auth_required
def update_client():
    client = Mapper.get_instance().json_to_client(request.json)
    try:
        client_service.update(client)
    except ValueError as err:
        return Response(err, 400)
    return Mapper.get_instance().client_to_json(client)


@clients.route('/clients', methods=['DELETE'])
@auth_required
def delete_clients():
    client_id = request.args.get('clientid')
    try:
        client_service.remove(client_id)
    except ValueError as err:
        return Response(err, 400)
    return jsonify(success=True)