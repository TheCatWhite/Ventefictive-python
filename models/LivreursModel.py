from config.ConnexionBase import ConnexionBase
class LivreursModel:
    def __init__(self,id_livreur,nomlivreur,contact_livreur):
        self.id_livreur = id_livreur
        self.nomlivreur = nomlivreur
        self.contact_livreur = contact_livreur
    @property
    def id_livreur(self):
        return self._id_livreur
    @id_livreur.setter
    def id_livreur(self,value):
        self._id_livreur=value
    @property
    def nomlivreur(self):
        return self._nomlivreur
    @nomlivreur.setter
    def nomlivreur(self,value):
        self._nomlivreur=value
    @property
    def contact_livreur(self):
        return self._contact_livreur
    @contact_livreur.setter
    def contact_livreur(self,value):
        self._contact_livreur=value
    def __str__(self):
        return f"Livreur(id_livreur={self.id_livreur}, nomlivreur={self.nomlivreur}, contact_livreur={self.contact_livreur})"
    
    @classmethod
    def getall(cls):
        ma_connexion = ConnexionBase.creer_connexion()
        livreurs = []
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return livreurs
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_livreur, nomlivreur, contact_livreur FROM livreurs"
            cursor.execute(chaine_req)
            rows = cursor.fetchall()
            for row in rows:
                livreur = LivreursModel(
                    id_livreur=row[0],
                    nomlivreur=row[1],
                    contact_livreur=row[2]
                )
                livreurs.append(livreur)
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return livreurs
    
    @classmethod
    def getbyid(cls,id):
        ma_connexion = ConnexionBase.creer_connexion()
        if ma_connexion is None:
            print("Erreur de connexion à la base de données")
            return None
        try:
            cursor = ma_connexion.cursor()
            chaine_req = "SELECT id_livreur, nomlivreur, contact_livreur FROM livreurs WHERE id_livreur = %s"
            cursor.execute(chaine_req, (id,))
            row = cursor.fetchone()
            if row:
                return cls(
                    id_livreur=row[0],
                    nomlivreur=row[1],
                    contact_livreur=row[2]
                )
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            cursor.close()
            ma_connexion.close()
        return None