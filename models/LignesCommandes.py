from config.ConnexionBase import ConnexionBase
class LignesCommandes:
    def __init__(self,id_ligne,id_produit,id_commande,quantite):
        self.id_ligne = id_ligne
        self.id_produit = id_produit
        self.id_commande = id_commande
        self.quantite = quantite
        
        
    @property
    def id_ligne(self):
        return self._id_ligne
    @id_ligne.setter
    def id_ligne(self,value):
        self._id_ligne=value
    @property
    def id_produit(self):
        return self._id_produit 
    @id_produit.setter
    def id_produit(self,value):
        self._id_produit=value
    @property
    def id_commande(self):
        return self._id_commande
    @id_commande.setter
    def id_commande(self,value):
        self._id_commande=value
    @property
    def quantite(self):
        return self._quantite
    @quantite.setter
    def quantite(self,value):
        self._quantite=value
    def __str__(self):
        return f"LigneCommande(id_ligne={self.id_ligne}, id_produit={self.id_produit}, id_commande={self.id_commande}, quantite={self.quantite})"
    
    @classmethod
    def getall(cls):
        ma_connexion = ConnexionBase.creer_connexion()
        lignes_commandes = []
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return lignes_commandes
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_ligne, id_produit, id_commande, quantite FROM lignes_commande"
            cursor.execute(chaine_req)
            rows = cursor.fetchall()
            for row in rows:
                ligne_commande = LignesCommandes(
                    id_ligne=row[0],
                    id_produit=row[1],
                    id_commande=row[2],
                    quantite=row[3]
                )
                lignes_commandes.append(ligne_commande)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return lignes_commandes
    
    
    @classmethod
    def getbyid(cls,id):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return None
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_ligne, id_produit, id_commande, quantite FROM lignes_commande WHERE id_ligne=%s"
            cursor.execute(chaine_req,(id,))
            row = cursor.fetchone()
            if row:
                ligne_commande = LignesCommandes(
                    id_ligne=row[0],
                    id_produit=row[1],
                    id_commande=row[2],
                    quantite=row[3]
                )
                return ligne_commande
            else:
                return None
        except Exception as e:
            print(f"Erreur : {e}")
            return None
        finally:
            cursor.close()
            ma_connexion.close()
            
    def insert(self):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return False
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "INSERT INTO lignes_commande (id_produit, id_commande, quantite) VALUES (%s, %s, %s)"
            cursor.execute(chaine_req, (self.id_produit, self.id_commande, self.quantite))
            ma_connexion.commit()
            self.id_ligne = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Erreur lors de l'insertion de la ligne de commande : {e}")
            ma_connexion.rollback()
            return False
        finally:
            cursor.close()
            ma_connexion.close()