

class UserRepository:
    def findByEmail(self,email):
        from domain.user import User
        return User.query.filter_by(email=email).first()