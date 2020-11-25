from controller import db
class ReportSession(db.Model):
    __tablename__='ReportSessions'
    __id=db.Column('id', db.Integer, primary_key=True)
    __project_id=db.Column(db.Integer, db.ForeignKey('Projects.id'))
    __user_id=db.Column(db.Integer, db.ForeignKey('Users.id'))
    __start_date=db.Column('start_date', db.Date)
    __end_date = db.Column('end_date', db.Date)
    __was_completed=db.Column('was_completed', db.Boolean)

    def __init__(self,id,project_id,user_id,start_date,end_date,was_completed):
        self.__id=id
        self.__project_id=project_id
        self.__user_id=user_id
        self.__start_date=start_date
        self.__end_date=end_date
        self.__was_completed=was_completed

    def get_id(self):
        return self.__id

    def get_project_id(self):
        return self.__project_id

    def get_user_id(self):
        return self.__user_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_was_completed(self):
        return self.__was_completed

    def set_user_id(self,value):
        self.__user_id=value

    def set_project_id(self, value):
        self.__project_id=value

    def set_start_date(self, value):
        self.__start_date=value

    def set_end_date(self, value):
        self.__end_date=value

    def set_was_completed(self,value):
        self.__was_completed=value

    def set_id(self, value):
        self.__id=value


