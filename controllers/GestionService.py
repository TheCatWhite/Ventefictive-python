from controllers.LivreurController import LivreurController
from controllers.CommandesController import CommandesController


class GestionService:
    def __init__(self):
        self.livreurs=LivreurController.lister_tous_les_livreurs()
        self.commandes=CommandesController.lister_toutes_les_commandes()
        
    def assigner_livreur_a_commande(self, id_livreur, id_commande):
        livreur = LivreurController.chercher_livreur(id_livreur)
        commande = CommandesController.afficher_une_commande(id_commande)
        
        if not livreur:
            print(f"\nErreur : Le livreur avec l'ID {id_livreur} n'existe pas.")
            return False
        if not commande:
            print(f"\nErreur : La commande avec l'ID {id_commande} n'existe pas.")
            return False
        if livreur.est_occupe():
            print(f"\nErreur : Le livreur {livreur.nom_livreur} est actuellement occupé.")
            return False
        if commande.est_livre:
            print(f"\nErreur : La commande n°{id_commande} a déjà été livrée.")
            return False
        
        succes = commande.assigner_livreur(id_livreur=id_livreur)
        if succes:
            print(f"\nSuccès : Le livreur {livreur.nom_livreur} a été assigné à la commande n°{id_commande}.")
        return succes
        