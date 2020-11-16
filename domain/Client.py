from controller import db


class Client(db.Model):
    __tablename__='Clients'
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String)
    __description = db.Column('description', db.String)

    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description

    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

    def set_description(self, value):
        self.__description = value

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

