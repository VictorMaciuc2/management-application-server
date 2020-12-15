import secrets
import string

from werkzeug.security import check_password_hash
import smtplib, ssl
from email.message import EmailMessage

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

        gmail_user = 'colectivgrupa3@gmail.com'  # trebuie introduse
        gmail_password = 'colectiv123!!!'        # cele corecte si adevarate ! ! !

        user.set_password(self.__get_generated_password())


        msg = EmailMessage()
        msg['Subject'] = 'Your password at our company.'
        msg['From'] = gmail_user
        # msg['To'] = user.get_email()
        msg['To'] = gmail_user  # trimit mail-ul pe acelasi cont pentru test
        msg.set_content('Hello, here is your password: ' + user.get_password())


        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user,gmail_password)
            #server.sendmail(sent_from,to,user.get_password()+"parola") #nu mere bine
            server.send_message(msg)

        except:
            return None
