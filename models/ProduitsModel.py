from config.ConnexionBase import ConnexionBase
class ProduitsModel:
    def __init__(self,id_produit,nom_produit,prix_produit,stock_produit,id_fournisseur):
        self.id_produit = id_produit
        self.nom_produit = nom_produit
        self.prix_produit = prix_produit
        self.stock_produit = stock_produit
        self.id_fournisseur = id_fournisseur
        
    @property
    def id_produit(self):
        return self._id_produit
    @id_produit.setter
    def id_produit(self,value):
        self._id_produit=value  
        
    @property
    def nom_produit(self):
        return self._nom_produit
    @nom_produit.setter
    def nom_produit(self,value):
        self._nom_produit=value
    @property
    def prix_produit(self):
        return self._prix_produit
    @prix_produit.setter
    def prix_produit(self,value):
        self._prix_produit=value
    @property
    def stock_produit(self):
        return self._stock_produit
    @stock_produit.setter
    def stock_produit(self,value):
        self._stock_produit=value
    @property
    def id_fournisseur(self):
        return self._id_fournisseur
    @id_fournisseur.setter
    def id_fournisseur(self,value):
        self._id_fournisseur=value
    def __str__(self):
        return f"Produit(id_produit={self.id_produit}, nom_produit={self.nom_produit}, prix_produit={self.prix_produit}, stock_produit={self.stock_produit}, id_fournisseur={self.id_fournisseur})"
    
    
    @classmethod
    def getall(cls):
        ma_connexion = ConnexionBase.creer_connexion()
        produits = []
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return produits
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_produit, nom_produit, prix_produit, stock_produit, id_fournisseur FROM produits"
            cursor.execute(chaine_req)
            rows = cursor.fetchall()
            for row in rows:
                produit = ProduitsModel(
                    id_produit=row[0],
                    nom_produit=row[1],
                    prix_produit=row[2],
                    stock_produit=row[3],
                    id_fournisseur=row[4]
                )
                produits.append(produit)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return produits
    
    @classmethod
    def getbyid(cls,id):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return None
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_produit, nom_produit, prix_produit, stock_produit, id_fournisseur FROM produits WHERE id_produit = %s"
            cursor.execute(chaine_req, (id,))
            row = cursor.fetchone()
            if row:
                produit=ProduitsModel(
                    id_produit=row[0],
                    nom_produit=row[1],
                    prix_produit=row[2],
                    stock_produit=row[3],
                    id_fournisseur=row[4]
                )
                return produit
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return None