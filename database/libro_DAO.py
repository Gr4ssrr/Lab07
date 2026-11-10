from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri_filtrati(self, biblioteca: str, genere: str) -> list[Libro]:
        """Restituisce i libri filtrati per nome biblioteca e/o genere (filtri opzionali, None = nessun filtro)."""
        connessione = DBConnect.get_connection()
        cursor = connessione.cursor()
        query = """
            SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca
            FROM libro l
            JOIN biblioteca b ON l.id_biblioteca = b.id
            WHERE b.nome = COALESCE(%s, b.nome) AND l.genere = COALESCE(%s, l.genere)
            ORDER BY l.titolo
        """
        cursor.execute(query, (biblioteca, genere))
        libri = [
            Libro(id=r[0], titolo=r[1], autore=r[2], genere=r[3], anno_pubblicazione=r[4], id_biblioteca=r[5])
            for r in cursor.fetchall()
        ]
        cursor.close()
        connessione.close()
        return libri

    def get_generi(self) -> list[str]:
        """Restituisce la lista di tutti i generi distinti dei libri."""
        connessione = DBConnect.get_connection()
        cursor = connessione.cursor()
        cursor.execute("SELECT DISTINCT genere FROM libro ORDER BY genere")
        generi = [riga[0] for riga in cursor.fetchall()]
        cursor.close()
        connessione.close()
        return generi
