from controller import db
class ReportSession(db.Model):
    __tablename__='ReportSessions'
    id=db.Column('id',db.Integer,primary_key=True)
    project_id=db.Column(db.Integer,db.ForeignKey('Projects.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('Users.id'))
    start_date=db.Column('start_date',db.Date)
    end_date = db.Column('end_date', db.Date)
    was_completed=db.Column('was_completed',db.Boolean)

    def __init__(self,id,project_id,user_id,start_date,end_date,was_completed):
        self.id=id
        self.project_id=project_id
        self.user_id=user_id
        self.start_date=start_date
        self.end_date=end_date
        self.was_completed=was_completed

    def get_id(self):
        return self.id

    def get_project_id(self):
        return self.project_id

    def get_user_id(self):
        return self.user_id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_was_completed(self):
        return self.was_completed

    def set_user_id(self,value):
        self.user_id=value

    def set_project_id(self, value):
        self.project_id=value

    def set_start_date(self, value):
        self.start_date=value

    def set_end_date(self, value):
        self.end_date=value

    def set_was_completed(self,value):
        self.was_completed=value

    def set_id(self, value):
        self.id=value


