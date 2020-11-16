
class UserService:
    def __init__(self,userRepository):
        self.userRepository = userRepository

    def matchUserPassword(self, user):
        email = user.get_email()
        addedUser = self.userRepository.findByEmail(email)
        if not user or user.password != addedUser.password:  # fara hashing
            return None  # if the user doesn't exist or password is wrong, return null

        return addedUser