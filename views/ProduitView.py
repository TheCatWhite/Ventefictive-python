import tkinter as tk
from tkinter import ttk, messagebox
from controllers.ProduitsController import ProduitsController

class ProduitView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white")
        self.pack(fill="both", expand=True)
        self.creer_widgets()

    def creer_widgets(self):
        tk.Label(self, text="Catalogue des Produits", font=("Arial", 18, "bold"), bg="white").pack(pady=15)

        # Zone d'actions
        actions_frame = tk.Frame(self, bg="white")
        actions_frame.pack(pady=10)
        
        tk.Label(actions_frame, text="ID Produit :", bg="white").pack(side="left", padx=5)
        self.entree_id = tk.Entry(actions_frame, highlightthickness=1)
        self.entree_id.pack(side="left", padx=5)
        
        # BOUTON 1 : Chercher
        tk.Button(actions_frame, text="Chercher", bg="#3498db", fg="white", 
                  command=self.chercher_produit).pack(side="left", padx=5)

        # BOUTON 2 : L'Analyse de stock (Ce que tu demandais)
        tk.Button(actions_frame, text="Analyser Stock", bg="#e67e22", fg="white", 
                  command=self.declencher_analyse_stock).pack(side="left", padx=5)

        # Tableau
        self.tree = ttk.Treeview(self, columns=("ID", "Nom", "Prix", "Stock", "Fournisseur"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Désignation")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Fournisseur", text="ID Fourn.")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

        tk.Button(self, text="Rafraîchir tout", command=self.charger_donnees).pack(pady=10)

    def charger_donnees(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        produits = ProduitsController.lister_tous_les_produits()
        for p in produits:
            self.tree.insert("", "end", values=(p.id_produit, p.nom_produit, p.prix_produit, p.stock_produit, p.id_fournisseur))

    def chercher_produit(self):
        id_p = self.entree_id.get()
        p = ProduitsController.chercher_produit_par_id(id_p)
        if p:
            for item in self.tree.get_children(): self.tree.delete(item)
            self.tree.insert("", "end", values=(p.id_produit, p.nom_produit, p.prix_produit, p.stock_produit, p.id_fournisseur))
        else:
            messagebox.showerror("Erreur", "Produit non trouvé")

    # --- NOUVELLE FONCTION POUR LE BOUTON D'ANALYSE ---
    def declencher_analyse_stock(self):
        id_p = self.entree_id.get()
        if not id_p:
            messagebox.showwarning("Attention", "Saisissez un ID produit pour l'analyse.")
            return

        # On appelle la fonction du controller qui fait les calculs
        est_disponible = ProduitsController.verifier_stock(id_p)
        
        # Pour informer l'utilisateur dans l'interface Tkinter
        produit = ProduitsController.chercher_produit_par_id(id_p)
        if produit:
            if produit.stock_produit <= 0:
                messagebox.showerror("Stock", f"ALERTE : {produit.nom_produit} est en rupture !")
            else:
                messagebox.showinfo("Analyse", f"Analyse terminée pour {produit.nom_produit}.\nConsultez la console pour le détail des seuils.")
        else:
            messagebox.showerror("Erreur", "Impossible d'analyser un produit inexistant.")