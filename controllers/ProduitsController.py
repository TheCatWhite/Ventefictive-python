from models.ProduitsModel import ProduitsModel

class ProduitsController:

    @staticmethod
    def lister_tous_les_produits():
        """Récupère tous les produits disponibles dans la base de données."""
        produits = ProduitsModel.getall()
        if not produits:
            print("\nAucun produit trouvé dans le catalogue.")
        return produits

    @staticmethod
    def chercher_produit_par_id(id_produit):
        """Recherche un produit spécifique par son ID."""
        if id_produit is None:
            print("\nErreur : L'identifiant du produit est requis.")
            return None
            
        produit = ProduitsModel.getbyid(id_produit)
        if not produit:
            print(f"\nErreur : Le produit avec l'ID {id_produit} n'existe pas.")
        
        return produit

    @staticmethod
    def verifier_stock(id_produit):
        produit = ProduitsController.chercher_produit_par_id(id_produit)
        prod=ProduitsController.lister_tous_les_produits()
        moy=sum(p.stock_produit for p in prod)/len(prod) if prod else 0
        if produit:
            if produit.stock_produit >= 10:
                print(f"\nStock disponible : {produit.stock_produit} unité(s) de '{produit.nom_produit}'.")
                return True
            elif produit.stock_produit > 0:
                print(f"\nAttention : Stock faible pour '{produit.nom_produit}' - seulement {produit.stock_produit} unité(s) restantes.")
                return True
            else:
                print(f"\nAttention : Le produit '{produit.nom_produit}' est en rupture de stock.")
                return False
        return False