from controller import db


class Report(db.Model):
    __tablename__='Reports'
    __id=db.Column('id', db.Integer, primary_key=True)
    __user_id=db.Column(db.Integer,db.ForeignKey('Users.id'))
    __skill_id = db.Column(db.Integer,db.ForeignKey('Skills.id'))
    __project_id=db.Column(db.Integer,db.ForeignKey('Projects.id'))
    __mark=db.Column('mark',db.Integer)
    __date=db.Column('date',db.Date)

    def __init__(self,id,name,description):
        self.__id=id
        self.__name=name
        self.__description=description


    def set_user_id(self,value):
        self.__user_id=value
    def set_skill_up(self,value):
        self.__skill_id=value
    def set_project_id(self,value):
        self.__project_id=value
    def set_mark(self,value):
        self.__project_id=value
    def set_date(self,value):
        self.__date=value

    def set_id(self, value):
        self.__id = value

    def get_id(self):
        return self.__id

    def get_user_id(self):
        return self.__user_id
    def get_skill_id(self):
        return self.__skill_id
    def get_project_id(self):
        return self.__project_id
    def get_mark(self):
        return self.__mark
    def get_date(self):
        return self.__date