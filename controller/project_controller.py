from flask import Blueprint
from flask import jsonify, request

from controller.mapper import Mapper
from repository.project_repository import ProjectRepository
from repository.technology_repository import TechnologyRepository
from repository.project_technology_repository import ProjectTechnologyRepository
from repository.user_project_repository import UserProjectRepository
from service.project_service import ProjectService
from service.technology_service import TechnologyService
from controller.client_controller import client_service

technology_service = TechnologyService(TechnologyRepository())
project_service = ProjectService(ProjectRepository(), ProjectTechnologyRepository(), UserProjectRepository(),
                                 technology_service, client_service)

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
    project_service.add(project)
    return Mapper.get_instance().project_to_json(project)


@projects.route('/projects', methods=['PUT'])
def update_project():
    project = Mapper.get_instance().json_to_project(request.json)
    project_service.update(project)
    return Mapper.get_instance().project_to_json(project)


@projects.route('/projects', methods=['DELETE'])
def delete_project():
    project_id = request.args.get('projectid')
    project_service.remove(project_id)
    return jsonify(success=True)
