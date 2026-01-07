import tkinter as tk
from tkinter import messagebox
from controllers.LignesCommandesController import LignesCommandesController

class FactureView(tk.Toplevel): # Toplevel pour ouvrir une fenêtre de reçu
    def __init__(self, id_commande):
        super().__init__()
        self.title(f"Facture N° {id_commande}")
        self.geometry("400x550")
        self.config(bg="#f8f9fa")
        self.id_commande = id_commande
        self.afficher_facture()

    def afficher_facture(self):
        donnees = LignesCommandesController.generer_facture(self.id_commande)
        
        if not donnees:
            messagebox.showerror("Erreur", "Aucun article dans cette commande.")
            self.destroy()
            return

        # Zone de texte pour la facture
        txt = tk.Text(self, font=("Courier", 10), bg="white", padx=20, pady=20)
        txt.pack(fill="both", expand=True)

        # Construction du design de la facture
        header = f"""
        ================================
               VENTE FICTIVE SARL
           123 Rue de l'Informatique
        ================================
        FACTURE N° : {donnees['id']}
        DATE       : 07/01/2026
        --------------------------------
        PRODUIT          QTÉ     TOTAL
        --------------------------------\n"""
        txt.insert("end", header)

        for l in donnees['lignes']:
            # Formatage des colonnes
            nom = l['nom'][:15].ljust(16)
            qty = str(l['qty']).center(5)
            st = f"{l['st']:.2f}€".rjust(10)
            txt.insert("end", f"{nom} {qty} {st}\n")

        footer = f"""
        --------------------------------
        TOTAL À PAYER :      {donnees['total']:.2f}€
        ================================
           Merci de votre confiance !
        ================================
        """
        txt.insert("end", footer)
        txt.config(state="disabled") # Empêcher l'édition

        tk.Button(self, text="Fermer", command=self.destroy, bg="#e74c3c", fg="white").pack(pady=10)