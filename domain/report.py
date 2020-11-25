from controller import db


class Report(db.Model):
    __tablename__='Reports'
    id=db.Column('id', db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('Users.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('Skills.id'))
    project_id=db.Column(db.Integer, db.ForeignKey('Projects.id'))
    mark=db.Column('mark', db.Integer)
    date=db.Column('date', db.Date)

    def __init__(self,id,name,description):
        self.id=id
        self.__name=name
        self.__description=description


    def set_user_id(self,value):
        self.user_id=value
    def set_skill_up(self,value):
        self.skill_id=value
    def set_project_id(self,value):
        self.project_id=value
    def set_mark(self,value):
        self.project_id=value
    def set_date(self,value):
        self.date=value

    def set_id(self, value):
        self.id = value

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id
    def get_skill_id(self):
        return self.skill_id
    def get_project_id(self):
        return self.project_id
    def get_mark(self):
        return self.mark
    def get_date(self):
        return self.date