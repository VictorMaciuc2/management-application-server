from controller import db

class User_Project(db.Model):
    __tablename__='User_Project'
    __id=db.Column('id',db.Integer,primary_key=True)
    __user_id=db.Column(db.Integer,db.ForeignKey('Users.id'))
    __project_id=db.Column(db.Integer,db.ForeignKey('Projects.id'))

    def __init__(self,id,user_id,project_id):
        self.__id=id
        self.__user_id=user_id
        self.__project_id=project_id

    def get_id(self):
        return self.__id
    def get_user_id(self):
        return self.__user_id
    def get_project_id(self):
        return self.__project_id
    def set_id(self,value):
        self.__id=value
    def set_user_id(self,value):
        self.__user_id=value
    def set_project_id(self,value):
        self.__project_id=value