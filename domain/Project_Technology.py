from controller import db


class Project_Technology(db.Model):
    __tablename__ = 'Project_Technology'
    __id = db.Column('id', db.Integer, primary_key=True)
    __technology_id = db.Column(db.Integer, db.ForeignKey('Technologies.id'))
    __project_id = db.Column(db.Integer, db.ForeignKey('Projects.id'))

    def __init__(self, id, user_id, project_id):
        self.__id = id
        self.__technology_id = user_id
        self.__project_id = project_id

    def get_id(self):
        return self.__id

    def get_technology_id(self):
        return self.__technology_id

    def get_project_id(self):
        return self.__project_id

    def set_id(self, value):
        self.__id = value

    def set_technology_id(self, value):
        self.__technology_id = value

    def set_project_id(self, value):
        self.__project_id = value