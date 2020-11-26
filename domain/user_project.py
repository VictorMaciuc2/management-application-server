from controller import db

class User_Project(db.Model):
    __tablename__='User_Project'
    id=db.Column('id', db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('Users.id'))
    project_id=db.Column(db.Integer, db.ForeignKey('Projects.id'))

    def __init__(self,id,user_id,project_id):
        self.id=id
        self.user_id=user_id
        self.project_id=project_id

    def get_id(self):
        return self.id
    def get_user_id(self):
        return self.user_id
    def get_project_id(self):
        return self.project_id
    def set_id(self,value):
        self.id=value
    def set_user_id(self,value):
        self.user_id=value
    def set_project_id(self,value):
        self.project_id=value