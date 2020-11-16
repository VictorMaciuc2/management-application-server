from domain import user
class UserRepository:

    def findByEmail(self,email):
        return user.User.query.filter_by(email=email).first()