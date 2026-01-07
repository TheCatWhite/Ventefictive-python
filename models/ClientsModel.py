from config.ConnexionBase import ConnexionBase

class ClientsModel:
    def __init__(self,id_client=None,nom_client=None,email_client=None,adress_client=None):
        self.id_client = id_client
        self.nom_client = nom_client
        self.email_client = email_client
        self.adress_client = adress_client
    

    @property
    def id_client(self):
        return self._id_client
    @id_client.setter
    def id_client(self,value):
        self._id_client=value
        
        
    @property
    def nom_client(self):
        return self._nom_client
    @nom_client.setter
    def nom_client(self,value):
        self._nom_client=value
        
    @property
    def email_client(self):
        return self._email_client
    @email_client.setter
    def email_client(self,value):
        self._email_client=value
        
    @property
    def adress_client(self):
        return self._adress_client
    @adress_client.setter
    def adress_client(self,value):
        self._adress_client=value
        
        
    
    
    
    def __str__(self):
        return f"Client(id_client={self.id_client}, nom_client={self.nom_client}, email_client={self.email_client}, adresse_client={self.adress_client})"
    
    @classmethod
    def getall(cls):
        ma_connexion = ConnexionBase.creer_connexion()
        clients = []
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return clients
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_client, nom_client, email_client, adresse_client FROM clients"
            cursor.execute(chaine_req)
            rows = cursor.fetchall()
            for row in rows:
                client = ClientsModel(
                    id_client=row[0],
                    nom_client=row[1],
                    email_client=row[2],
                    adress_client=row[3],
                )
                clients.append(client)
        except Exception as e:
            print(f"Erreur lors de la lecture des clients : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return clients
    
    
    @classmethod
    def getbyid(cls, id):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            return None
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_client, nom_client, email_client, adresse_client FROM clients WHERE id_client = %s"
            cursor.execute(chaine_req, (id,))
            row = cursor.fetchone()
            if row:
                client=ClientsModel(
                    id_client=row[0],
                    nom_client=row[1],
                    email_client=row[2],
                    adress_client=row[3]
                )
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close() 
            ma_connexion.close()
        return client
                    
                