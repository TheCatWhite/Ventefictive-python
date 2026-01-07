import tkinter as tk
from tkinter import ttk, messagebox
from controllers.LivreurController import LivreursController

class LivreurView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white")
        self.pack(fill="both", expand=True)
        self.creer_widgets()

    def creer_widgets(self):
        # Titre
        tk.Label(self, text="Gestion des Livreurs", font=("Arial", 18, "bold"), bg="white").pack(pady=15)

        # Zone d'actions et recherche
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(pady=10)
        
        tk.Label(search_frame, text="ID Livreur :", bg="white").pack(side="left", padx=5)
        self.entree_id = tk.Entry(search_frame, highlightthickness=1)
        self.entree_id.pack(side="left", padx=5)
        
        # Bouton Chercher
        tk.Button(search_frame, text="🔍 Chercher", bg="#e67e22", fg="white", 
                  command=self.chercher_livreur).pack(side="left", padx=5)

        # NOUVEAU : Bouton pour voir uniquement les disponibles
        tk.Button(search_frame, text="✅ Voir Dispo", bg="#27ae60", fg="white", 
                  command=self.afficher_disponibles).pack(side="left", padx=5)

        # Tableau des livreurs
        self.tree = ttk.Treeview(self, columns=("ID", "Nom", "Contact"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom complet")
        self.tree.heading("Contact", text="Coordonnées / Téléphone")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nom", width=200)
        self.tree.column("Contact", width=200)
        
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

        # Bouton Rafraîchir (Tout afficher)
        tk.Button(self, text="Afficher tous les livreurs", bg="#34495e", fg="white",
                  command=self.charger_donnees).pack(pady=15)

    def charger_donnees(self):
        """Affiche la liste complète des livreurs."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        livreurs = LivreursController.lister_tous_les_livreurs()
        for l in livreurs:
            # Note : j'utilise l.nom_livreur comme défini dans ton modèle
            self.tree.insert("", "end", values=(l.id_livreur, l.nom_livreur, l.contact_livreur))

    def afficher_disponibles(self):
        """Filtre le tableau pour n'afficher que les livreurs disponibles."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Appel de ta nouvelle fonction dans le controller
        dispos = LivreursController.livreurs_disponibles()
        
        if not dispos:
            messagebox.showinfo("Information", "Aucun livreur disponible pour le moment.")
        
        for l in dispos:
            self.tree.insert("", "end", values=(l.id_livreur, l.nom_livreur, l.contact_livreur))

    def chercher_livreur(self):
        id_l = self.entree_id.get()
        if not id_l:
            messagebox.showwarning("Attention", "Veuillez entrer un ID livreur.")
            return
            
        l = LivreursController.chercher_livreur(id_l)
        if l:
            for item in self.tree.get_children(): self.tree.delete(item)
            self.tree.insert("", "end", values=(l.id_livreur, l.nom_livreur, l.contact_livreur))
        else:
            messagebox.showerror("Erreur", "Livreur introuvable.")