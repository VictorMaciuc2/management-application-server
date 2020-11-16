from controller import db
class Project(db.Model):
    __tablename__='Projects'
    __id=db.Column('id', db.Integer, primary_key=True)
    __name=db.Column('name', db.String)
    __description = db.Column('description', db.String)
    __start_date=db.Column('start_date', db.Date)
    __end_date = db.Column('end_date', db.Date)
    __deadline_date = db.Column('deadline_date', db.Date)
    __client_id = db.Column(db.Integer, db.ForeignKey("Clients.id"))

    def __init__(self,id,name,description,start_date,end_date,deadline_date,client_id):
        self.__id=id
        self.__name=name
        self.__description=description
        self.__deadline_date=deadline_date
        self.__client_id=client_id
        self.__start_date=start_date
        self.__deadline_date=end_date


    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_name(self):
        return self.__name

    def get_client_id(self):
        return self.__client_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__deadline_date

    def get_deadline_date(self):
        return self.__deadline_date

    def set_client_id(self,value):
        self.__client_id=value

    def set_start_date(self, value):
        self.__start_date=value

    def set_end_date(self, value):
        self.__deadline_date=value

    def set_deadline_date(self,value):
        self.__deadline_date=value

    def set_id(self, value):
        self.__id=value

    def set_name(self,value):
        self.__name=value

    def set_description(self,value):
        self.value=value



