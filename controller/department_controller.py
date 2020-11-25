from flask import Blueprint
from flask import jsonify, request
from controller.mapper import Mapper
from repository.department_repository import DepartmentRepository
from service.department_service import DepartmentService


department_repo = DepartmentRepository()
department_service = DepartmentService(department_repo)

deps = Blueprint('deps',__name__)


@deps.route('/departments', methods=['GET'])
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


@deps.route('/departments', methods=['POST'])
def save_department():
    department = Mapper.get_instance().json_to_department(request.json)
    department_service.add(department)
    return Mapper.get_instance().department_to_json(department)


@deps.route('/departments', methods=['PUT'])
def update_department():
    department = Mapper.get_instance().json_to_department(request.json)
    department_service.update(department)
    return Mapper.get_instance().department_to_json(department)


@deps.route('/departments', methods=['DELETE'])
def delete_departments():
    department_id = request.args.get('departmentid')
    department_service.remove(department_id)
    return jsonify(success=True)
