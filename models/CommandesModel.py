from config.ConnexionBase import ConnexionBase
class CommandesModel:
    def __init__(self,id_commande=None,id_client=None,date_commande=None,est_livre=None,id_livreur=None):
        self.id_commande = id_commande
        self.id_client = id_client
        self.date_commande = date_commande
        self.est_livre = est_livre
        self.id_livreur = id_livreur
        
        
    @property
    def id_commande(self):
        return self._id_commande
    @id_commande.setter
    def id_commande(self,value):
        self._id_commande=value
    @property
    def id_client(self):
        return self._id_client
    @id_client.setter
    def id_client(self,value):
        self._id_client=value
    @property
    def date_commande(self):
        return self._date_commande
    @date_commande.setter
    def date_commande(self,value):
        self._date_commande=value
    @property
    def est_livre(self):
        return self._est_livre
    @est_livre.setter
    def est_livre(self,value):
        self._est_livre=value
    @property
    def id_livreur(self):
        return self._id_livreur
    @id_livreur.setter
    def id_livreur(self,value):
        self._id_livreur=value
    def __str__(self):
        return f"Commande(id_commande={self.id_commande}, id_client={self.id_client}, date_commande={self.date_commande}, est_livre={self.est_livre}, id_livreur={self.id_livreur})"
    
    
    @classmethod
    def getall(cls):
        ma_connexion = ConnexionBase.creer_connexion()
        commandes = []
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return commandes
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_commande, id_client, date_commande, est_livre, id_livreur FROM commandes"
            cursor.execute(chaine_req)
            rows = cursor.fetchall()
            for row in rows:
                commande = CommandesModel(
                    id_commande=row[0],
                    id_client=row[1],
                    date_commande=row[2],
                    est_livre=row[3],
                    id_livreur=row[4]
                )
                commandes.append(commande)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return commandes
    
    @classmethod
    def getbyid(cls,id):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return None
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_commande, id_client, date_commande, est_livre, id_livreur FROM commandes WHERE id_commande = %s"
            cursor.execute(chaine_req, (id,))
            row = cursor.fetchone()
            if row:
                commande=CommandesModel(
                    id_commande=row[0],
                    id_client=row[1],
                    date_commande=row[2],
                    est_livre=row[3],
                    id_livreur=row[4]
                )
                return commande
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return None
    
    
    def mark_as_delivered(self):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return False
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "UPDATE commandes SET est_livre = TRUE WHERE id_commande = %s"
            cursor.execute(chaine_req, (self.id_commande,))
            ma_connexion.commit()
            self.est_livre = True
            return True
        except Exception as e:
            print(f"Erreur lors de la mise à jour du statut de livraison : {e}")
            return False
        finally:
            cursor.close()
            ma_connexion.close()
            
    def delete(self):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return False
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "DELETE FROM commandes WHERE id_commande = %s"
            cursor.execute(chaine_req, (self.id_commande,))
            ma_connexion.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de la suppression de la commande : {e}")
            return False
        finally:
            cursor.close()
            ma_connexion.close()