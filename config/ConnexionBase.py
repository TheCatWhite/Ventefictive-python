import psycopg2
class ConnexionBase:

    @staticmethod
    def creer_connexion():
        try:
            return psycopg2.connect(
                user="postgres",
                password="Rabary182606",
                host="127.0.0.1",
                port="5432",
                database="ventefictive"
            )

        except Exception as e:
            raise Exception(f"Erreur de connexion à la base de données : {e}")
