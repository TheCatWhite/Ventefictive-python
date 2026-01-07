from models.LivreursModel import LivreursModel

class LivreursController:

    @staticmethod
    def lister_tous_les_livreurs():
        livreurs = LivreursModel.getall()
        if not livreurs:
            print("\nAucun livreur n'est enregistré dans le système.")
        return livreurs

    @staticmethod
    def chercher_livreur(id_livreur):
        if id_livreur is None:
            print("\nErreur : Un identifiant de livreur est nécessaire.")
            return None
            
        livreur = LivreursModel.getbyid(id_livreur)
        if not livreur:
            print(f"\nErreur : Le livreur avec l'ID {id_livreur} n'existe pas.")
        
        return livreur

    @staticmethod
    def verifier_disponibilite(id_livreur):
        livreur = LivreursController.chercher_livreur(id_livreur)
        if livreur:
            print(f"\nContact pour {livreur.nomlivreur} : {livreur.contact_livreur}")
            return True
        return False
    
    
    @staticmethod
    def livreurs_occupees():
        livreurs = LivreursController.lister_tous_les_livreurs()
        livres_occupees = []
        for livreur in livreurs:
            if livreur.est_occupe():
                livres_occupees.append(livreur)
        return livres_occupees
    
    @staticmethod
    def livreurs_disponibles():
        livreurs = LivreursController.lister_tous_les_livreurs()
        livres_disponibles = []
        for livreur in livreurs:
            if not livreur.est_occupe():
                livres_disponibles.append(livreur)
        return livres_disponibles
        