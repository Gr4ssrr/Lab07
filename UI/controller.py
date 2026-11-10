import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        """Legge da modello biblioteche e generi e popola i relativi dropdown nella view."""
        biblioteche = self._model.get_biblioteche()
        self._view.popola_dropdown_biblioteche(biblioteche)

        generi = self._model.get_generi()
        self._view.popola_dropdown_generi(generi)

    # CALLBACKS DROPDOWN
    def seleziona_biblioteca(self, e):
        """Memorizza la biblioteca selezionata (None se 'Nessun filtro')."""
        valore = e.control.value
        self.biblioteca_selezionata = None if valore == "Nessun filtro" else valore

    def seleziona_genere(self, e):
        """Memorizza il genere selezionato (None se 'Nessun filtro')."""
        valore = e.control.value
        self.genere_selezionato = None if valore == "Nessun filtro" else valore

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        """Richiede al modello i libri filtrati secondo le selezioni correnti e li mostra nella view."""
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if not libri:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati.")
        else:
            self._view.mostra_libri(libri)
