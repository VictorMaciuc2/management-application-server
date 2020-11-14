from controller import db
from domain.Client import Client

class RepositoryClient:

    def getAll(self):
        '''
        :return: list of clients
        '''
        clients = Client.query.all()
        return clients

    def getOne(self,id):
        '''
        :param id: int
        :return: Client
        '''
        client = Client.query.get(id)
        return client

    def add(self,Client):
        '''
        :param Client: Client
        :return:
        '''
        db.session.add(Client)
        db.session.commit()

    def remove(self,client):
        '''
        :param Client: Client
        :return:
        '''
        db.session.delete(client)
        db.session.commit()

    def update(self,client):
        '''
        :param client: Client
        :return:
        '''
        clientfound = Client.query.get(client.get_id())
        clientfound.set_name(client.get_name())
        clientfound.set_description(client.get_description())
        db.session.commit()