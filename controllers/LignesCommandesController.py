from models.LignesCommandes import LignesCommandes

class LignesCommandesController:

    @staticmethod
    def lister_toutes_les_lignes():
        """Récupère absolument toutes les lignes de commandes enregistrées."""
        lignes = LignesCommandes.getall()
        if not lignes:
            print("\nAucune ligne de commande trouvée.")
        return lignes

    @staticmethod
    def chercher_ligne_par_id(id_ligne):
        """Récupère une ligne spécifique via son identifiant unique."""
        ligne = LignesCommandes.getbyid(id_ligne)
        if not ligne:
            print(f"\nErreur : La ligne n°{id_ligne} est introuvable.")
        return ligne

    @staticmethod
    def ajouter_produit_a_commande(id_produit, id_commande, quantite):
        """
        Crée et insère une nouvelle ligne de commande.
        Vérifie que la quantité est valide avant l'insertion.
        """
        if quantite <= 0:
            print("\nErreur : La quantité doit être supérieure à 0.")
            return False

        nouvelle_ligne = LignesCommandes(None, id_produit, id_commande, quantite)
        
        if nouvelle_ligne.insert():
            print(f"\nSuccès : Produit {id_produit} ajouté à la commande {id_commande}.")
            return True
        else:
            print("\nErreur : Impossible d'ajouter le produit à la commande.")
            return False

    @staticmethod
    def filtrer_par_commande(id_commande):
        toutes = LignesCommandes.getall()
        lignes_specifiques = [l for l in toutes if l.id_commande == id_commande]
        
        if not lignes_specifiques:
            print(f"\nAucun produit trouvé pour la commande n°{id_commande}.")
        
        return lignes_specifiques