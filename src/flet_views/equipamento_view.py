import flet as ft

class EquipamentoView(ft.Container):

    def __init__(self, page):

        super().__init__()
        
        self.expand = True
        self.padding = 30
        self.content = ft.Text(
            "Equipamentos"
        )