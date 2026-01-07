from config.ConnexionBase import ConnexionBase
from models.FournisseurModel import FournisseurModel
from models.ProduitsModel import ProduitsModel
from controllers.ClientsController import ClientsController
from models.ClientsModel import ClientsModel
from controllers.CommandesController import CommandesController
if __name__ == "__main__":
    if ConnexionBase.creer_connexion():
        print("Connexion réussie à la base de données.")
    else:
        print("Échec de la connexion à la base de données.")
        
    clients=ClientsController.lister_clients()
    for l in clients:
        print(l)
        
    client=ClientsController.getbyid(202)
    print(client)

    
    fourniseur=FournisseurModel.getbyid(55)
    print(fourniseur)
    
    commandes=CommandesController.lister_commandes()
    for c in commandes:
        print(c)