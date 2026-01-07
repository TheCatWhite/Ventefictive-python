-- Création de la base (à faire à part si tu es déjà connecté à une base)
-- CREATE DATABASE donnees_vente_fictives;

-- --------------------------------------------------------
-- Table `clients`
-- --------------------------------------------------------
CREATE TABLE clients (
  id_client SERIAL PRIMARY KEY,
  nom_client varchar(50) DEFAULT NULL,
  email_client varchar(50) DEFAULT NULL,
  adresse_client varchar(50) DEFAULT NULL
);

INSERT INTO clients (id_client, nom_client, email_client, adresse_client) VALUES
(201, 'Rakoto', 'rakoto@gmail.com', 'Lot AF 5 Anosipatrana'),
(202, 'Rabe', 'rabe123@gmail.com', 'Villa milay Ambohijanahary'),
(203, 'Rasoa', 'rsoa@gmail.com', 'Lot V-32 Analakely');

-- --------------------------------------------------------
-- Table `fournisseurs`
-- --------------------------------------------------------
CREATE TABLE fournisseurs (
  id_fournisseur SERIAL PRIMARY KEY,
  nom_fournisseur varchar(50) DEFAULT NULL
);

INSERT INTO fournisseurs (id_fournisseur, nom_fournisseur) VALUES
(54, 'BureauNet'),
(55, 'SanitaireFourniture'),
(56, 'Tana Market'),
(57, 'Technologia');

-- --------------------------------------------------------
-- Table `livreurs`
-- --------------------------------------------------------
CREATE TABLE livreurs (
  id_livreur SERIAL PRIMARY KEY,
  nom_livreur varchar(50) DEFAULT NULL,
  contact_livreur char(10) DEFAULT NULL
);

INSERT INTO livreurs (id_livreur, nom_livreur, contact_livreur) VALUES
(51, 'Rasolo be', '0345711132'),
(52, 'Ketaka kely', '0321765866');

-- --------------------------------------------------------
-- Table `produits`
-- --------------------------------------------------------
CREATE TABLE produits (
  id_produit SERIAL PRIMARY KEY,
  nom_produit varchar(50) DEFAULT NULL,
  prix_produit int DEFAULT NULL,
  stock_produit int DEFAULT NULL,
  id_fournisseur int REFERENCES fournisseurs(id_fournisseur)
);

INSERT INTO produits (id_produit, nom_produit, prix_produit, stock_produit, id_fournisseur) VALUES
(564, 'Chargeur', 5000, 85, 56),
(566, 'Smartphone 114', 2000000, 10, 56),
(567, 'Smartphone 322', 2500000, 5, 56),
(568, 'Chargeur rapide', 10000, 25, 54),
(569, 'Efferalgan', 2000, 180, 55),
(570, 'Cahier', 2000, 250, 57);

-- --------------------------------------------------------
-- Table `commandes`
-- --------------------------------------------------------
CREATE TABLE commandes (
  id_commande SERIAL PRIMARY KEY,
  id_client int REFERENCES clients(id_client),
  date_commande date DEFAULT NULL,
  est_livre boolean DEFAULT FALSE,
  id_livreur int REFERENCES livreurs(id_livreur)
);

INSERT INTO commandes (id_commande, id_client, date_commande, est_livre, id_livreur) VALUES
(1034, 202, '2025-07-10', FALSE, 52),
(1035, 202, '2025-07-10', FALSE, 52);

-- --------------------------------------------------------
-- Table `lignes_commande`
-- --------------------------------------------------------
CREATE TABLE lignes_commande (
  id_ligne SERIAL PRIMARY KEY,
  id_produit int REFERENCES produits(id_produit),
  id_commande int REFERENCES commandes(id_commande),
  quantite int DEFAULT NULL
);

INSERT INTO lignes_commande (id_ligne, id_produit, id_commande, quantite) VALUES
(1, 567, 1034, 10),
(2, 568, 1034, 5),
(3, 569, 1035, 20),
(4, 564, 1035, 15);