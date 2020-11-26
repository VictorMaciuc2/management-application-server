from flask import Blueprint
from flask import jsonify, request

from repository.project_repository import ProjectRepository
from controller.mapper import Mapper
from service.project_service import ProjectService
from controller.client_controller import client_service

project_repo = ProjectRepository()
project_service = ProjectService(project_repo)

projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=['GET'])
def get_all_projects():
    project_id = request.args.get('projectid')
    if project_id is None:
        return jsonify([Mapper.get_instance().project_to_json(x) for x in project_service.getAll()])
    else:
        return Mapper.get_instance().project_to_json(project_service.getOne(project_id))


@projects.route('/projects', methods=['POST'])
def save_project():
    project = Mapper.get_instance().json_to_project(request.json)
    __check_project_client(project)
    project_service.add(project)
    return Mapper.get_instance().project_to_json(project)


@projects.route('/projects', methods=['PUT'])
def update_project():
    project = Mapper.get_instance().json_to_project(request.json)
    __check_project_client(project)
    project_service.update(project)
    return Mapper.get_instance().project_to_json(project)


@projects.route('/projects', methods=['DELETE'])
def delete_project():
    project_id = request.args.get('projectid')
    project_service.remove(project_id)
    return jsonify(success=True)


def __check_project_client(project):
    if client_service.getOne(project.get_client_id()) is None:  # crapa de pe linia asta
        raise ValueError("The client with the given ID does not exist.")
