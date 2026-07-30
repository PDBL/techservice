import flet as ft

class EquipamentoView(ft.Container):

    def __init__(self):

        super().__init__()

        self.expand = True

        self.padding = 25

        self.content = ft.Text(
            "Equipamentos"
        )