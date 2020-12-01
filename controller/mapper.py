from datetime import datetime


class Mapper:
    __instance = None
    __date_format = '%Y-%m-%d'  # YYYY-MM-DD

    def __init__(self):
        Mapper.__instance = self

    @staticmethod
    def get_instance():
        if Mapper.__instance is None:
            return Mapper()
        return Mapper.__instance

    def json_to_client(self, json):
        from domain.client import Client
        return Client(json['id'], json['name'], json['description'])

    def json_to_department(self, json):
        from domain.department import Department
        return Department(json['id'], json['name'], json['description'])

    def json_to_user(self, json):
        from domain.user import User
        return User(json['id'], json['name'], json['email'], None, json['role'], json['seniorityLevel'],
                    json['departmentId'])

    def json_to_project(self, json):
        from domain.project import Project
        return Project(json['id'], json['name'], json['description'],
                       datetime.strptime(json['start_date'], Mapper.__date_format),
                       datetime.strptime(json['end_date'], Mapper.__date_format),
                       datetime.strptime(json['deadline_date'], Mapper.__date_format), json['client_id'])

    def json_to_technology(self, json):
        from domain.technology import Technology
        return Technology(json['id'], json['name'])

    def client_to_json(self, client):
        return {'id': client.id, 'name': client.name, 'description': client.description}

    def department_to_json(self, department):
        return {'id': department.id, 'name': department.name, 'description': department.description}

    def user_to_json(self, user):
        return {'id': user.id, 'email': user.email, 'name': user.name, 'role': user.role,
                'seniorityLevel': user.seniority_level, 'departmentId': user.department_id,
                'department': self.department_to_json(user.department)}

    def project_to_json(self, project):
        return {'id': project.get_id(), 'name': project.get_name(), 'description': project.get_description(),
                'start_date': project.get_start_date().strftime(Mapper.__date_format),
                'end_date': project.get_end_date().strftime(Mapper.__date_format),
                'deadline_date': project.get_deadline_date().strftime(Mapper.__date_format),
                'client_id': project.get_client_id()}

    def technology_to_json(self, tech):
        return {'id': tech.get_id(), 'name': tech.get_name()}
   