import string

from domain.Client import Client

class ServiceClient(object):

    def __init__(self, __repo):
        self.__repo = __repo

    def add(self,id,name,description ):
        '''
        :param id: int
        :param name: string
        :param description: string
        :return:
        raises value error if id already exists
        '''
        if not(isinstance ( id, int)):
            raise ValueError("id is not an integer")
        if not(isinstance ( name, str)):
            raise ValueError("name is not a string")
        if not(isinstance ( description, str)):
            raise ValueError("description is not a string")

        client = self.__repo.getOne(self.__repo,id)
        if (client != None):
            raise ValueError("Already exists a client with given id")
        client = Client(id,name,description)
        self.__repo.add(self.__repo,client)

    def getAll(self):
        '''
        :return: lists of clients
        '''
        clients =  self.__repo.getAll(self.__repo)
        return clients

    def getOne(self,id):
        '''
        :param id: int
        :return: Client
         raises value error if id does not exist
        '''
        client = self.__repo.getOne(self.__repo,id)
        if(client==None):
            raise ValueError("Client with given id does not exist.")
        return client

    def remove(self,id):
        '''
        removes client by id
        :param id: int
        :return:
        raise value error if id does not exist.
        '''
        client = self.__repo.getOne(self.__repo, id)
        if (client == None):
            raise ValueError("Client with given id does not exist.")
        self.__repo.remove(self.__repo,client)

    def update(self,client):
        '''
        updates client
        :param Client: client
        :return:
        raise value error if id does not exist.
        '''
        clientfound = self.__repo.getOne(self.__repo, client.get_id())
        if (clientfound == None):
            raise ValueError("Client with given id does not exist.")

        self.__repo.update(self.__repo,client)
