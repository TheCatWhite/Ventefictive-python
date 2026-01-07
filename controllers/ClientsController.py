from models.ClientsModel import ClientsModel

class ClientsController:
    
    @classmethod    
    def lister_clients(cls):
        client = ClientsModel()
        return client.getall()
    
    @classmethod
    def getbyid(cls, id_client):
        if not id_client:
            raise ValueError("L'ID du client ne peut pas être vide.")
        client = ClientsModel(id_client)
        return client.getbyid(id_client)