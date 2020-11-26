import secrets
import string

from werkzeug.security import check_password_hash
import smtplib, ssl

class UserService:
    def __init__(self,__repo):
        self.__repo = __repo

    def matchUserPassword(self, email, password):
        addedUser = self.__repo.findByEmail(email)
        if not addedUser or addedUser.get_password() != password:
                # TODO: Skip for now: (check_password_hash(addedUser.get_password(), password) is False):  # verify hash
            return None  # if the user doesn't exist or password is wrong, return null
        return addedUser

    def add(self,user):
        userfound = self.__repo.getOne(user.get_id())
        if (userfound != None):
            raise ValueError("Already exists a user with given id")
        return self.__repo.add(user)

    def getAll(self):
        users =  self.__repo.getAll()
        return users

    def getOne(self,id):
        user = self.__repo.getOne(id)
        if(user==None):
            raise ValueError("User with given id does not exist.")
        return user

    def remove(self,id):
        user = self.__repo.getOne(id)
        if (user == None):
            raise ValueError("User with given id does not exist.")
        self.__repo.remove(user)

    def update(self,user):
        userfound = self.__repo.getOne(user.get_id())
        if (userfound == None):
            raise ValueError("User with given id does not exist.")

        self.__repo.update(user)

        return user

    def __get_generated_password(self):
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for i in range(20))


    def send_password_email(self,user):

        gmail_user = 'adresaHRului@gmail.com'  # trebuie introduse
        gmail_password = 'parolaHRului'        # cele corecte si adevarate ! ! !

        sent_from = gmail_user
        to = [user.get_email()]
        user.set_password(self.__get_generated_password())
        subject = 'Your password at our company.'
        body = 'Hello, here is your password: ' + user.get_password()

        email_text="""\
        From: %s
        To: %s
        Subject: %s
        
        %s
        
        
        This is an automated e-mail. Please do not reply.
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user,gmail_password)
            server.sendmail(sent_from,to,body)
        except:
            return None
