class ClientService:

    def __init__(self, __repo):
        self.__repo = __repo

    def add(self,client):
        '''
        :param client: Client
        :return:
        raises value error if client already exists
        '''
        clientfound = self.__repo.getOne(client.get_id())
        if (clientfound != None):
            raise ValueError("Already exists a client with given id")
        return self.__repo.add(client)

    def getAll(self):
        '''
        :return: lists of clients
        '''
        clients =  self.__repo.getAll()
        return clients

    def getOne(self,id):
        '''
        :param id: int
        :return: Client
         raises value error if id does not exist
        '''
        client = self.__repo.getOne(id)
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
        client = self.__repo.getOne(id)
        if (client == None):
            raise ValueError("Client with given id does not exist.")
        self.__repo.remove(client)

    def update(self,client):
        '''
        updates client
        :param Client: client
        :return:
        raise value error if id does not exist.
        '''
        clientfound = self.__repo.getOne(client.get_id())
        if (clientfound == None):
            raise ValueError("Client with given id does not exist.")

        self.__repo.update(client)

        return client
