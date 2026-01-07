from models.FournisseurModel import FournisseurModel

class FournisseurController:

    @staticmethod
    def lister_tous_les_fournisseurs():
        fournisseurs = FournisseurModel.getall()
        if not fournisseurs:
            print("\nAucun fournisseur trouvé dans la base de données.")
        return fournisseurs

    @staticmethod
    def chercher_fournisseur_par_id(id_fournisseur):
        if not id_fournisseur:
            print("\nErreur : L'ID du fournisseur est requis.")
            return None
            
        fournisseur = FournisseurModel.getbyid(id_fournisseur)
        if fournisseur:
            return fournisseur
        else:
            print(f"\nErreur : Aucun fournisseur trouvé avec l'ID {id_fournisseur}.")
            return None