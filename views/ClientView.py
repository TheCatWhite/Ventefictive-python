import tkinter as tk
from tkinter import ttk, messagebox
from controllers.ClientsController import ClientsController

class ClientView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.creer_widgets()

    def creer_widgets(self):
        tk.Label(self, text="Gestion des Clients", font=("Arial", 18, "bold")).pack(pady=10)

        # Zone de recherche
        search_frame = tk.Frame(self)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="ID Client:").pack(side="left")
        self.entree_id = tk.Entry(search_frame)
        self.entree_id.pack(side="left", padx=5)
        tk.Button(search_frame, text="Chercher", command=self.chercher_client).pack(side="left")

        # Tableau des clients
        self.tree = ttk.Treeview(self, columns=("ID", "Nom", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Email", text="Email")
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        # Bouton Charger
        tk.Button(self, text="Actualiser la liste", command=self.charger_donnees).pack(pady=5)

    def charger_donnees(self):
        # Nettoyer le tableau
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        
        clients = ClientsController.lister_clients()
        for c in clients:
            self.tree.insert("", "end", values=(c.id_client, c.nom_client, c.email_client))

    def chercher_client(self):
        id_c = self.entree_id.get()
        if not id_c:
            messagebox.showwarning("Attention", "Veuillez entrer un ID")
            return
        
        client = ClientsController.getbyid(id_c)
        if client:
            for item in self.tree.get_children(): self.tree.delete(item)
            self.tree.insert("", "end", values=(client.id_client, client.nom_client, client.email_client))
        else:
            messagebox.showerror("Erreur", "Client non trouvé")