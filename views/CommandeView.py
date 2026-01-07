import tkinter as tk
from tkinter import ttk, messagebox
from controllers.CommandesController import CommandesController

class CommandeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white")
        self.pack(fill="both", expand=True)
        self.creer_widgets()

    def creer_widgets(self):
        # Titre principal
        tk.Label(self, text="Gestion des Commandes", font=("Arial", 18, "bold"), bg="white").pack(pady=15)

        # Barre d'outils (Boutons d'action)
        toolbar = tk.Frame(self, bg="white")
        toolbar.pack(pady=10, fill="x", padx=30)

        tk.Button(toolbar, text="✅ Valider Livraison", bg="#2ecc71", fg="white", font=("Arial", 10, "bold"),
                  command=self.action_livrer).pack(side="left", padx=5)

        tk.Button(toolbar, text="🗑️ Supprimer", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                  command=self.action_supprimer).pack(side="left", padx=5)

        tk.Button(toolbar, text="🔄 Actualiser", bg="#34495e", fg="white",
                  command=self.charger_donnees).pack(side="right", padx=5)

        tk.Button(toolbar, text="📄 Voir Facture", bg="#9b59b6", fg="white", 
          command=self.ouvrir_facture).pack(side="left", padx=5)
        # Tableau des commandes
        self.tree = ttk.Treeview(self, columns=("ID", "Client", "Date", "Statut", "Livreur"), show="headings")
        self.tree.heading("ID", text="N° Commande")
        self.tree.heading("Client", text="ID Client")
        self.tree.heading("Date", text="Date de Commande")
        self.tree.heading("Statut", text="Statut Livraison")
        self.tree.heading("Livreur", text="ID Livreur")

        # Configuration des colonnes
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Statut", width=150, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

    def charger_donnees(self):
        """Récupère les commandes via le controller et remplit le tableau."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        commandes = CommandesController.lister_toutes_les_commandes()
        for c in commandes:
            statut = "LIVRÉ" if c.est_livre else "EN COURS"
            self.tree.insert("", "end", values=(c.id_commande, c.id_client, c.date_commande, statut, c.id_livreur))

    def action_livrer(self):
        """Récupère l'ID sélectionné et valide la livraison."""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Sélection", "Veuillez sélectionner une commande.")
            return

        id_commande = self.tree.item(selection[0])['values'][0]
        if messagebox.askyesno("Confirmation", f"Marquer la commande n°{id_commande} comme livrée ?"):
            if CommandesController.valider_livraison(id_commande):
                messagebox.showinfo("Succès", "Livraison validée !")
                self.charger_donnees()

    def action_supprimer(self):
        """Récupère l'ID sélectionné et supprime la commande."""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Sélection", "Veuillez sélectionner une commande.")
            return

        id_commande = self.tree.item(selection[0])['values'][0]
        if messagebox.askyesno("Attention", f"Voulez-vous vraiment supprimer la commande n°{id_commande} ?"):
            if CommandesController.supprimer_commande(id_commande):
                messagebox.showinfo("Suppression", "Commande supprimée avec succès.")
                self.charger_donnees()
                
    def get_selection(self):
            """Récupère l'ID de la commande sélectionnée dans le tableau."""
            selection = self.tree.selection() # Vérifie si une ligne est surlignée
            if not selection:
                messagebox.showwarning("Sélection", "Veuillez sélectionner une commande dans le tableau.")
                return None
            
            # item(selection[0]) récupère toutes les données de la ligne
            # ['values'][0] récupère l'ID (première colonne)
            valeurs = self.tree.item(selection[0])['values']
            return valeurs[0]

    def ouvrir_facture(self):
        """Déclenche l'affichage de la fenêtre facture."""
        id_c = self.get_selection() 
        if id_c:
            from views.FactureView import FactureView
            FactureView(id_c)