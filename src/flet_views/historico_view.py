import flet as ft

class HistoricoView(ft.Container):

    def __init__(self):

        super().__init__()

        self.expand = True

        self.padding = 25

        self.content = ft.Text(
            "Histórico"
        )