import tkinter as tk
from tkinter import ttk, messagebox
from controllers.CommandesController import CommandesController
from controllers.LivreurController import LivreursController

class CommandeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white")
        self.pack(fill="both", expand=True)
        self.creer_widgets()

    def creer_widgets(self):
        # --- TITRE ---
        tk.Label(self, text="Gestion des Commandes", font=("Arial", 18, "bold"), bg="white").pack(pady=15)

        # --- BARRE D'OUTILS ---
        toolbar = tk.Frame(self, bg="white")
        toolbar.pack(pady=10, fill="x", padx=30)

        # Boutons d'action
        tk.Button(toolbar, text="✅ Valider Livraison", bg="#2ecc71", fg="white", font=("Arial", 9, "bold"),
                  command=self.action_livrer).pack(side="left", padx=5)
        tk.Button(toolbar, text="❌ Annuler Livraison", bg="#e74c3c", fg="white", font=("Arial", 9, "bold"),
                  command=self.nonaction_livrer).pack(side="left", padx=5)

        tk.Button(toolbar, text="🚚 Assigner Livreur", bg="#3498db", fg="white", font=("Arial", 9, "bold"),
                  command=self.ouvrir_fenetre_assignation).pack(side="left", padx=5)

        tk.Button(toolbar, text="📄 Voir Facture", bg="#9b59b6", fg="white", font=("Arial", 9, "bold"),
                  command=self.ouvrir_facture).pack(side="left", padx=5)

        tk.Button(toolbar, text="🗑️ Supprimer", bg="#e74c3c", fg="white", font=("Arial", 9, "bold"),
                  command=self.action_supprimer).pack(side="left", padx=5)

        # Bouton Actualiser à droite
        tk.Button(toolbar, text="🔄 Actualiser", bg="#34495e", fg="white",
                  command=self.charger_donnees).pack(side="right", padx=5)

        # --- TABLEAU (TREEVIEW) ---
        self.tree = ttk.Treeview(self, columns=("ID", "Client", "Date", "Statut", "Livreur"), show="headings")
        self.tree.heading("ID", text="N° Commande")
        self.tree.heading("Client", text="ID Client")
        self.tree.heading("Date", text="Date de Commande")
        self.tree.heading("Statut", text="Statut Livraison")
        self.tree.heading("Livreur", text="ID Livreur Assigné")

        # Configuration visuelle des colonnes
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Client", width=100, anchor="center")
        self.tree.column("Statut", width=150, anchor="center")
        self.tree.column("Livreur", width=120, anchor="center")
        
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

    def charger_donnees(self):
        """Récupère et affiche la liste des commandes."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        commandes = CommandesController.lister_toutes_les_commandes()
        for c in commandes:
            statut = "LIVRÉ" if c.est_livre else "EN COURS"
            # Si id_livreur est None, on affiche 'Non assigné'
            livreur_display = c.id_livreur if c.id_livreur else "---"
            self.tree.insert("", "end", values=(c.id_commande, c.id_client, c.date_commande, statut, livreur_display))

    def get_selection(self):
        """Fonction utilitaire pour récupérer l'ID de la ligne sélectionnée."""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Sélection", "Veuillez sélectionner une commande dans le tableau.")
            return None
        return self.tree.item(selection[0])['values'][0]

    def action_livrer(self):
        id_c = self.get_selection()
        if id_c:
            if messagebox.askyesno("Livraison", f"Confirmer la livraison de la commande {id_c} ?"):
                if CommandesController.valider_livraison(id_c):
                    messagebox.showinfo("Succès", "Commande marquée comme livrée.")
                    self.charger_donnees()
    
    def nonaction_livrer(self):
        id_c = self.get_selection()
        if id_c:
            if messagebox.askyesno("Livraison", f"Annuler la livraison de la commande {id_c} ?"):
                if CommandesController.invalider_livraison(id_c):
                    messagebox.showinfo("Succès", "Commande marquée comme en cours.")
                    self.charger_donnees()

    def action_supprimer(self):
        id_c = self.get_selection()
        if id_c:
            if messagebox.askyesno("Confirmation", f"Supprimer définitivement la commande {id_c} ?"):
                if CommandesController.supprimer_commande(id_c):
                    messagebox.showinfo("Suppression", "Commande supprimée.")
                    self.charger_donnees()

    def ouvrir_facture(self):
        id_c = self.get_selection()
        if id_c:
            from views.FactureView import FactureView
            FactureView(id_c)

    # --- LOGIQUE D'ASSIGNATION DE LIVREUR ---

    def ouvrir_fenetre_assignation(self):
        id_commande = self.get_selection()
        if not id_commande:
            return

        commande = CommandesController.afficher_une_commande(id_commande)
        if commande.est_livre:
            messagebox.showwarning("Erreur", "Impossible d'assigner un livreur à une commande déjà livrée.")
            return

        # Création de la fenêtre popup
        self.popup = tk.Toplevel(self)
        self.popup.title("Assignation Livreur")
        self.popup.geometry("350x250")
        self.popup.config(padx=20, pady=20)
        self.popup.grab_set() # Bloque l'accès à la fenêtre principale

        tk.Label(self.popup, text=f"Assigner un livreur à la commande #{id_commande}", font=("Arial", 10, "bold")).pack(pady=10)

        # Récupération des livreurs disponibles via le controller
        livreurs_dispos = LivreursController.livreurs_disponibles()
        
        if not livreurs_dispos:
            tk.Label(self.popup, text="Aucun livreur disponible !", fg="red").pack(pady=20)
            tk.Button(self.popup, text="Fermer", command=self.popup.destroy).pack()
            return

        # Dictionnaire pour lier le nom affiché à l'ID réel
        self.dict_livreurs = {f"{l.nom_livreur} (ID: {l.id_livreur})": l.id_livreur for l in livreurs_dispos}
        
        tk.Label(self.popup, text="Sélectionnez un livreur libre :").pack(anchor="w")
        self.combo_livreurs = ttk.Combobox(self.popup, values=list(self.dict_livreurs.keys()), state="readonly")
        self.combo_livreurs.pack(pady=10, fill="x")

        tk.Button(self.popup, text="💾 Confirmer l'assignation", bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: self.valider_assignation(id_commande)).pack(pady=15, fill="x")

    def valider_assignation(self, id_commande):
        selection_nom = self.combo_livreurs.get()
        if not selection_nom:
            messagebox.showwarning("Erreur", "Veuillez choisir un livreur dans la liste.")
            return

        id_livreur = self.dict_livreurs[selection_nom]
        commande = CommandesController.afficher_une_commande(id_commande)
        
        # On suppose que la méthode assigner_livreur existe dans CommandesModel
        if commande.assigner_livreur(id_livreur):
            messagebox.showinfo("Succès", f"Livreur {id_livreur} assigné avec succès !")
            self.popup.destroy()
            self.charger_donnees()
        else:
            messagebox.showerror("Erreur", "Échec de l'assignation en base de données.")