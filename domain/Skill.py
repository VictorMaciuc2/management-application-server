from controller import db


class Skill(db.Model):
    __tablename__='Skills'
    id=db.Column('id',db.Integer,primary_key=True)
    name=db.Column('name',db.String)

    def __init__(self,id,data):
        self.id=id
        self.data=data
