from config.ConnexionBase import ConnexionBase
class FournisseurModel:
    def __init__(self,id_fournisseur=None,nom_fournisseur=None):
        self.id_fournisseur = id_fournisseur
        self.nom_fournisseur = nom_fournisseur
        
    @property
    def id_fournisseur(self):
        return self._id_fournisseur
    @id_fournisseur.setter
    def id_fournisseur(self,value):
        self._id_fournisseur=value
    
    @property
    def nom_fournisseur(self):
        return self._nom_fournisseur
    @nom_fournisseur.setter
    def nom_fournisseur(self,value):
        self._nom_fournisseur=value
        
    def __str__(self):
        return f"Fournisseur(id_fournisseur={self.id_fournisseur}, nom_fournisseur={self.nom_fournisseur})"
    
    @classmethod
    def getall(cls):
        ma_connexion = ConnexionBase.creer_connexion()
        fournisseurs = []
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return fournisseurs
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_fournisseur, nom_fournisseur FROM fournisseurs"
            cursor.execute(chaine_req)
            rows = cursor.fetchall()
            for row in rows:
                fournisseur = FournisseurModel(
                    id_fournisseur=row[0],
                    nom_fournisseur=row[1]
                )
                fournisseurs.append(fournisseur)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return fournisseurs
    
    @classmethod
    def getbyid(cls,id):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return None
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_fournisseur, nom_fournisseur FROM fournisseurs WHERE id_fournisseur = %s"
            cursor.execute(chaine_req, (id,))
            row = cursor.fetchone()
            if row:
                fournisseur=FournisseurModel(
                    id_fournisseur=row[0],
                    nom_fournisseur=row[1]
                )
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close() 
            ma_connexion.close()
        return fournisseur