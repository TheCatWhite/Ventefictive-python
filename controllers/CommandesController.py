from models.CommandesModel import CommandesModel

class CommandesController:
    
    @staticmethod
    def lister_toutes_les_commandes():
        commandes = CommandesModel.getall()
        if not commandes:
            print("\nAucune commande trouvée.")
        return commandes

    @staticmethod
    def afficher_une_commande(id_commande):
        commande = CommandesModel.getbyid(id_commande)
        if commande:
            return commande
        else:
            print(f"\nErreur : La commande n°{id_commande} n'existe pas.")
            return None

    @staticmethod
    def valider_livraison(id_commande):
        commande = CommandesModel.getbyid(id_commande)
        if commande:
            if commande.est_livre:
                print(f"\nInfo : La commande n°{id_commande} est déjà marquée comme livrée.")
                return False
            
            succes = commande.mark_as_delivered()
            if succes:
                print(f"\nSuccès : La commande n°{id_commande} est maintenant livrée.")
            return succes
        else:
            print(f"\nErreur : Impossible de livrer une commande inexistante (ID: {id_commande}).")
            return False

    @staticmethod
    def invalider_livraison(id_commande):
        commande = CommandesModel.getbyid(id_commande)
        if commande:
            
            succes = commande.mark_as_not_delivered()
            if succes:
                print(f"\nSuccès : La commande n°{id_commande} est maintenant en cours.")
            return succes
        else:
            print(f"\nErreur : Impossible de livrer une commande inexistante (ID: {id_commande}).")
            return False  

    @staticmethod
    def supprimer_commande(id_commande):
        """Supprime une commande après confirmation de son existence."""
        commande = CommandesModel.getbyid(id_commande)
        if commande:
            succes = commande.delete()
            if succes:
                print(f"\nSuccès : La commande n°{id_commande} a été supprimée.")
            return succes
        else:
            print(f"\nErreur : Impossible de supprimer la commande n°{id_commande} (introuvable).")
            return False

    @staticmethod
    def assigner_livreur(id_commande, id_livreur):
        commande = CommandesModel.getbyid(id_commande)
        if commande:
            return commande.update(id_commande, commande.id_client, commande.date_commande, commande.est_livre, id_livreur)
        return False