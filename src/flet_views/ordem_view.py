import flet as ft

class OrdemView(ft.Container):

    def __init__(self):

        super().__init__()

        self.expand = True

        self.padding = 25

        self.content = ft.Text(
            "Ordens de Serviço"
        )