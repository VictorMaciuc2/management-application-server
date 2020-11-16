class ClientService:
    def __init__(self, __repo):
        self.__repo = __repo

    def add(self,client):
        clientfound = self.__repo.getOne(client.get_id())
        if (clientfound != None):
            raise ValueError("Already exists a client with given id")
        return self.__repo.add(client)

    def getAll(self):
        clients =  self.__repo.getAll()
        return clients

    def getOne(self,id):
        client = self.__repo.getOne(id)
        if(client==None):
            raise ValueError("Client with given id does not exist.")
        return client

    def remove(self,id):
        client = self.__repo.getOne(id)
        if (client == None):
            raise ValueError("Client with given id does not exist.")
        self.__repo.remove(client)

    def update(self,client):
        clientfound = self.__repo.getOne(client.get_id())
        if (clientfound == None):
            raise ValueError("Client with given id does not exist.")

        self.__repo.update(client)

        return client
