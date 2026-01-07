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