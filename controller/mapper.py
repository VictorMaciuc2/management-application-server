

class Mapper:
    __instance = None

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
        return User(json['email'], json['email'])

    def client_to_json(self, client):
        return {'id': client.id, 'name': client.name, 'description': client.description}

    def department_to_json(self, department):
        return {'id': department.id, 'name': department.name, 'description': department.description}

    def user_to_json(self, user):
        return {'id': user.id, 'email': user.email, 'name': user.name, 'role': user.role, 'seniority_level': user.seniority_level, 'department_id': user.department_id}



