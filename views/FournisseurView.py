import tkinter as tk
from tkinter import ttk, messagebox
from controllers.FournisseurController import FournisseurController

class FournisseurView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white")
        self.pack(fill="both", expand=True)
        self.creer_widgets()

    def creer_widgets(self):
        # Titre
        tk.Label(self, text="Gestion des Fournisseurs", font=("Arial", 18, "bold"), bg="white").pack(pady=15)

        # Zone de recherche
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(pady=10)
        
        tk.Label(search_frame, text="ID Fournisseur :", bg="white").pack(side="left", padx=5)
        self.entree_id = tk.Entry(search_frame, highlightthickness=1)
        self.entree_id.pack(side="left", padx=5)
        
        tk.Button(search_frame, text="Chercher", bg="#2980b9", fg="white", 
                  command=self.chercher_fournisseur).pack(side="left", padx=5)

        # Tableau (Treeview)
        self.tree = ttk.Treeview(self, columns=("ID", "Nom"), show="headings")
        self.tree.heading("ID", text="ID Fournisseur")
        self.tree.heading("Nom", text="Nom de l'entreprise")
        
        # Ajustement des colonnes
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Nom", width=400)
        
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

        # Bouton d'action
        tk.Button(self, text="Rafraîchir la liste", bg="#27ae60", fg="white", font=("Arial", 10, "bold"),
                  padx=20, pady=5, command=self.charger_donnees).pack(pady=15)

    def charger_donnees(self):
        """Récupère tous les fournisseurs via le Controller."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        fournisseurs = FournisseurController.lister_tous_les_fournisseurs()
        for f in fournisseurs:
            self.tree.insert("", "end", values=(f.id_fournisseur, f.nom_fournisseur))

    def chercher_fournisseur(self):
        """Cherche un fournisseur spécifique par son ID."""
        id_f = self.entree_id.get()
        if not id_f:
            messagebox.showwarning("Attention", "Veuillez saisir un ID.")
            return
            
        f = FournisseurController.chercher_fournisseur_par_id(id_f)
        if f:
            for item in self.tree.get_children(): self.tree.delete(item)
            self.tree.insert("", "end", values=(f.id_fournisseur, f.nom_fournisseur))
        else:
            messagebox.showinfo("Résultat", "Aucun fournisseur trouvé.")