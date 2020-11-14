from domain import User
class UserRepository:

    def findByEmail(email):
        return User.User.query.filter_by(email=email).first()