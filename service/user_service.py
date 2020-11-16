
class UserService:

    def __init__(self,userRepository):
        self.userRepository = userRepository

    def matchUserPassword(self,userDat):
        email = userDat.email
        user = self.userRepository.findByEmail(email)
        if not user or userDat.password != user.password:  # fara hashing
            # flash('Please check your login details and try again.')
            return None  # if the user doesn't exist or password is wrong, return null
        return user