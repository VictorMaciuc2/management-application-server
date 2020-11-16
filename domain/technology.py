from controller import db
class Technology(db.Model):
    __tablename__="Technologies"
    __id=db.Column('id', db.Integer, primary_key=True)
    __name=db.Column('name', db.String)

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
