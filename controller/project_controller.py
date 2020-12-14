from flask import Blueprint
from flask import jsonify, request

from controller.mapper import Mapper
from repository.project_repository import ProjectRepository
from repository.technology_repository import TechnologyRepository
from repository.project_technology_repository import ProjectTechnologyRepository
from repository.user_project_repository import UserProjectRepository
from service.project_service import ProjectService
from service.technology_service import TechnologyService
from controller.user_controller import user_service
from controller.client_controller import client_service
from controller.department_controller import department_service

technology_service = TechnologyService(TechnologyRepository())
project_service = ProjectService(ProjectRepository(), ProjectTechnologyRepository(), UserProjectRepository(),
                                 technology_service, user_service, client_service)

projects = Blueprint('projects', __name__)
__tech_path = '/projects/technologies'
__users_path = '/projects/users'
__tech_users_path = '/users/technologies'


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
            [Mapper.get_instance().technology_to_json(x) for x in
             project_service.getTechnologiesForProject(project_id)])

    if project_id is None:
        return Mapper.get_instance().technology_to_json(technology_service.getOne(tech_id))

    return jsonify(assigned=project_service.isTechAssignedToProject(project_id, tech_id))


# O tehnologie nu poate exista daca nu e asignata la minimum 1 proiect
# Daca nu exista deja, tehnologia e creata si adaugata
@projects.route(__tech_path, methods=['POST'])
def assign_techs():
    project_id = request.args.get('projectid')
    techs = Mapper.get_instance().json_to_technologies(request.json)
    for tech in techs:
        project_service.assignTechToProject(project_id, tech)
    return jsonify(success=True)


@projects.route(__tech_path, methods=['DELETE'])
def unassign_tech():
    project_id = request.args.get('projectid')
    tech_id = request.args.get('techid')
    project_service.unassignTechFromProject(project_id, tech_id)
    return jsonify(success=True)


@projects.route(__users_path, methods=['GET'])
def get_users():
    project_id = request.args.get('projectid')
    user_id = request.args.get('userid')
    if project_id is not None and user_id is not None:
        return jsonify(assigned=project_service.isUserAssignedToProject(project_id, user_id))

    if project_id is not None:
        users = project_service.getUsersForProject(project_id)
        return jsonify(
            [Mapper.get_instance().user_to_json(x, department_service.getOne(x.get_department_id())) for x in users])

    if user_id is not None:
        return jsonify([Mapper.get_instance().project_to_json(x) for x in project_service.getProjectsForUser(user_id)])


@projects.route(__users_path, methods=['POST'])
def assign_users():
    project_id = request.args.get('projectid')
    for user in request.json['users']:
        project_service.assignUserToProject(project_id, user['id'])
    return jsonify(success=True)


@projects.route(__users_path, methods=['DELETE'])
def unassign_user():
    project_id = request.args.get('projectid')
    user_id = request.args.get('userid')
    project_service.unassignUserFromProject(project_id, user_id)
    return jsonify(success=True)

@projects.route(__tech_users_path, methods=['GET'])
def get_users_by_technology():
    return jsonify(project_service.get_technologies_and_users_with_recommandation())
