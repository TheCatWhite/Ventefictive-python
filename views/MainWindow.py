import tkinter as tk
from views.ClientView import ClientView
from views.FournisseurView import FournisseurView
from views.ProduitView import ProduitView
from views.LivreurView import LivreurView
from views.CommandeView import CommandeView # Nouvel import

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Système de Gestion Commerciale")
        self.geometry("1100x700")

        # Sidebar
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=220)
        self.sidebar.pack(side="left", fill="y")
        
        # Container principal
        self.container = tk.Frame(self, bg="white")
        self.container.pack(side="right", fill="both", expand=True)

        self.current_view = None
        self.creer_menu()
        
        # Vue par défaut
        self.show_view(ClientView)

    def creer_menu(self):
        tk.Label(self.sidebar, text="MENU PRINCIPAL", fg="white", bg="#2c3e50", 
                 font=("Arial", 12, "bold")).pack(pady=20)
        
        # Liste des modules pour le menu
        menu_items = [
            ("👥 Clients", ClientView),
            ("🏢 Fournisseurs", FournisseurView),
            ("📦 Produits", ProduitView),
            ("🚚 Livreurs", LivreurView),
            ("📜 Commandes", CommandeView) # Nouvelle ligne
        ]

        for text, view_class in menu_items:
            btn = tk.Button(self.sidebar, text=text, font=("Arial", 11),
                            bg="#2c3e50", fg="white", relief="flat", padx=20, pady=12,
                            anchor="w", cursor="hand2",
                            command=lambda vc=view_class: self.show_view(vc))
            btn.pack(fill="x", pady=2)
            
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#34495e"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#2c3e50"))

        tk.Button(self.sidebar, text="🚪 Quitter", command=self.quit, 
                  bg="#c0392b", fg="white", relief="flat", pady=10).pack(side="bottom", fill="x")

    def show_view(self, view_class):
        """Détruit la vue actuelle et affiche la nouvelle."""
        if self.current_view is not None:
            self.current_view.destroy()
        
        self.current_view = view_class(self.container)
        # On rafraîchit les données automatiquement à l'ouverture de la vue
        if hasattr(self.current_view, 'charger_donnees'):
            self.current_view.charger_donnees()
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()