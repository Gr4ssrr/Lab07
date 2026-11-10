import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dropdown_biblioteca = ft.Dropdown(
            label="Biblioteca",
            hint_text="Seleziona una biblioteca",
            width=300,
            on_select=self.controller.seleziona_biblioteca,
        )
        self.dropdown_genere = ft.Dropdown(
            label="Genere",
            hint_text="Seleziona un genere",
            width=300,
            on_select=self.controller.seleziona_genere,
        )

        # Sezione 3: Libri
        self.btn_mostra_libri = ft.Button(
            content="Mostra Libri",
            on_click=self.controller.mostra_libri,
        )
        self.lista_libri = ft.ListView(
            expand=True,
            spacing=10,
            padding=10,
            height=400,
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(
                controls=[self.dropdown_biblioteca, self.dropdown_genere],
                alignment=ft.MainAxisAlignment.CENTER,
            ),

            # Sezione 3: Libri
            self.btn_mostra_libri,
            self.lista_libri,
        )

        self.page.scroll = "adaptive"
        self.page.update()

        self.controller.popola_dropdown()

    def popola_dropdown_biblioteche(self, biblioteche):
        """Popola il dropdown delle biblioteche con l'opzione 'Nessun filtro' e le biblioteche lette dal DB."""
        self.dropdown_biblioteca.options.clear()
        self.dropdown_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for biblioteca in biblioteche:
            self.dropdown_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))
        self.page.update()

    def popola_dropdown_generi(self, generi):
        """Popola il dropdown dei generi con l'opzione 'Nessun filtro' e i generi letti dal DB."""
        self.dropdown_genere.options.clear()
        self.dropdown_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for genere in generi:
            self.dropdown_genere.options.append(ft.dropdown.Option(genere))
        self.page.update()

    def mostra_libri(self, libri):
        """Popola la ListView con i libri passati."""
        self.lista_libri.controls.clear()
        for libro in libri:
            self.lista_libri.controls.append(ft.Text(str(libro)))
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
