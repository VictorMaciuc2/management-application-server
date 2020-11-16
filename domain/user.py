from controller import db


class User(db.Model):
    __tablename__='Users'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    email = db.Column('email', db.String)
    password = db.Column('password', db.String)
    role = db.Column('role', db.String)
    seniority_level=db.Column('seniority_level', db.String)
    department_id = db.Column(db.Integer, db.ForeignKey('Departments.id'))

    def __init__(self,id,name,email,password,role,seniority_level,department_id):
        self.id=id
        self.name=name
        self.email=email
        self.password=password
        self.role=role
        self.seniority_level=seniority_level
        self.department_id=department_id

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def set_id(self,value):
        self.__id=value

    def set_name(self, value):
        self.__name=value

    def set_email(self, value):
        self.email=value

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
        return self.email

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

    def get_seniority_level(self):
        return self.__seniority_level

    def get_department_id(self):
        return self.__department_id
