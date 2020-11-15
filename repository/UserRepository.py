from domain import User
class UserRepository:

    def findByEmail(self,email):
        return User.User.query.filter_by(email=email).first()