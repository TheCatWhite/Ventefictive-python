from models.LignesCommandes import LignesCommandes
from controllers.ProduitsController import ProduitsController

class LignesCommandesController:

    @staticmethod
    def lister_toutes_les_lignes():
        return LignesCommandes.getall()

    @staticmethod
    def filtrer_par_commande(id_commande):
        toutes = LignesCommandes.getall()
        return [l for l in toutes if l.id_commande == id_commande]

    @staticmethod
    def ajouter_produit_a_commande(id_produit, id_commande, quantite):
        if quantite <= 0: return False
        nouvelle_ligne = LignesCommandes(None, id_produit, id_commande, quantite)
        return nouvelle_ligne.insert()

    @staticmethod
    def generer_facture(id_commande):
        """Calcule les détails complets pour l'affichage de la facture."""
        lignes = LignesCommandesController.filtrer_par_commande(id_commande)
        if not lignes: return None
        
        total = 0
        details = []
        for ligne in lignes:
            produit = ProduitsController.chercher_produit_par_id(ligne.id_produit)
            if produit:
                sous_total = produit.prix_produit * ligne.quantite
                total += sous_total
                details.append({
                    'nom': produit.nom_produit,
                    'qty': ligne.quantite,
                    'pu': produit.prix_produit,
                    'st': sous_total
                })
        
        return {'id': id_commande, 'lignes': details, 'total': total}