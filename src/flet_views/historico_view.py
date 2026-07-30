import flet as ft

class HistoricoView(ft.Container):

    def __init__(self, page):

        super().__init__()

        self.expand = True
        self.padding = 30
        self.content = ft.Text(
            "Histórico"
        )