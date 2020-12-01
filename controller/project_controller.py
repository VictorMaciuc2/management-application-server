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
__tech_path = '/projects/technologies'


@projects.route('/projects', methods=['GET'])
def get_all_projects():
    project_id = request.args.get('projectid')
    if project_id is None:
        return jsonify([Mapper.get_instance().project_to_json(x) for x in project_service.getAllProjects()])
    else:
        return Mapper.get_instance().project_to_json(project_service.getOneProject(project_id))


@projects.route('/projects', methods=['POST'])
def save_project():
    project = Mapper.get_instance().json_to_project(request.json)
    project_service.addProject(project)
    return Mapper.get_instance().project_to_json(project)


@projects.route('/projects', methods=['PUT'])
def update_project():
    project = Mapper.get_instance().json_to_project(request.json)
    project_service.updateProject(project)
    return Mapper.get_instance().project_to_json(project)


@projects.route('/projects', methods=['DELETE'])
def delete_project():
    project_id = request.args.get('projectid')
    project_service.removeProject(project_id)
    return jsonify(success=True)


@projects.route(__tech_path, methods=['GET'])
def get_technologies():
    project_id = request.args.get('projectid')
    tech_id = request.args.get('techid')
    if project_id is None and tech_id is None:
        return jsonify([Mapper.get_instance().technology_to_json(x) for x in technology_service.getAll()])

    if tech_id is None:
        return jsonify(
            [Mapper.get_instance().technology_to_json(x) for x in project_service.getTechnologiesForProject(project_id)])

    return Mapper.get_instance().technology_to_json(technology_service.getOne(tech_id))


# O tehnologie nu poate exista daca nu e asignata la minimum 1 proiect
# Daca nu exista deja, tehnologia e creata si adaugata
# Returneaza tehnologia pentru a putea lua noul ID in caz ca a fost creata
@projects.route(__tech_path, methods=['POST'])
def assign_tech():
    project_id = request.args.get('projectid')
    tech = Mapper.get_instance().json_to_technology(request.json)
    project_service.assign_tech_to_project(project_id, tech)
    return Mapper.get_instance().technology_to_json(tech)


@projects.route(__tech_path, methods=['DELETE'])
def unassign_tech():
    project_id = request.args.get('projectid')
    tech_id = request.args.get('techid')
    project_service.unassign_tech_from_project(project_id, tech_id)
    return jsonify(success=True)
