import tkinter as tk
from views.MainWindow import MainWindow

def main():
    try:
        # Initialisation de la fenêtre principale Tkinter
        app = MainWindow()
        
        # Icône ou configuration optionnelle supplémentaire ici
        # app.iconbitmap("icon.ico") 
        
        print("Application démarrée avec succès...")
        
        # Lancement de la boucle infinie de l'interface
        app.mainloop()
        
    except Exception as e:
        print(f"Erreur lors du lancement de l'application : {e}")

if __name__ == "__main__":
    main()