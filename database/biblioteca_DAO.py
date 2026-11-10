from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self) -> list[Biblioteca]:
        """Restituisce la lista di tutte le biblioteche presenti nel database."""
        connessione = DBConnect.get_connection()
        cursor = connessione.cursor()
        cursor.execute("SELECT id, nome, indirizzo FROM biblioteca ORDER BY nome")
        biblioteche = [Biblioteca(id=riga[0], nome=riga[1], indirizzo=riga[2]) for riga in cursor.fetchall()]
        cursor.close()
        connessione.close()
        return biblioteche
