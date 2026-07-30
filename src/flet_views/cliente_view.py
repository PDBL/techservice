import flet as ft

class ClienteView(ft.Container):

    def __init__(self, page):

        super().__init__()

        self.expand = True
        self.padding = 30
        self.content = ft.Column(
            [
                ft.Text(
                    "Clientes",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Divider(),
                ft.Text(
                    ""
                )
            ]
        )