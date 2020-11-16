from controller import db


class User(db.Model):
    __tablename__='Users'
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String)
    __email = db.Column('email', db.String)
    __password = db.Column('password', db.String)
    __role = db.Column('role', db.String)
    __seniority_level=db.Column('seniority_level', db.String)
    __department_id = db.Column(db.Integer, db.ForeignKey('Departments.id'))

    def __init__(self,id,name,email,password,role,seniority_level,department_id):
        self.__id=id
        self.__name=name
        self.__email=email
        self.__password=password
        self.__role=role
        self.__seniority_level=seniority_level
        self.__department_id=department_id

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def set_id(self,value):
        self.__id=value

    def set_name(self, value):
        self.__name=value

    def set_email(self, value):
        self.__email=value

    def set_password(self, value):
        self.__password=value

    def set_role(self,value):
        self.__role=value

    def set_seniority_level(self, value):
        self.__seniority_level=value

    def set_department_id(self, value):
        self.__department_id=value

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

    def get_seniority_level(self):
        return self.__seniority_level

    def get_department_id(self):
        return self.__department_id
