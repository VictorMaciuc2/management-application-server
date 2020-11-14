class ServiceClient:

    def __init__(self, __repo):
        self.__repo = __repo

    def add(self,client):
        '''
        :param client: Client
        :return:
        raises value error if client already exists
        '''
        clientfound = self.__repo.getOne(self.__repo,client.get_id())
        if (clientfound != None):
            raise ValueError("Already exists a client with given id")
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
