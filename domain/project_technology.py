from controller import db


class Project_Technology(db.Model):
    __tablename__ = 'Project_Technology'
    project_id = db.Column(db.Integer, db.ForeignKey('Projects.id'), primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('Technologies.id'), primary_key=True)

    def __init__(self, user_id, project_id):
        self.technology_id = user_id
        self.project_id = project_id

    def get_technology_id(self):
        return self.technology_id

    def get_project_id(self):
        return self.project_id

    def set_technology_id(self, value):
        self.technology_id = value

    def set_project_id(self, value):
        self.project_id = value
