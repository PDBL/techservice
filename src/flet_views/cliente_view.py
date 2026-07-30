import flet as ft

class ClienteView(ft.Container):

    def __init__(self):
        super().__init__()

        self.expand = True
        self.padding = 20

        self.content = ft.Column(
            expand=True,
            controls=[
                self._cabecalho(),
                ft.Divider(),
                ft.Row(
                    expand=True,
                    spacing=20,
                    controls=[
                        self._painel_formulario(),
                        self._painel_lista(),
                    ],
                ),
            ],
        )

    def _cabecalho(self):

        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    spacing=2,
                    controls=[
                        ft.Text(
                            "Gestão de Clientes",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Sistema TechService",
                            color=ft.Colors.GREY_700,
                        ),
                    ],
                ),
                ft.Container(
                    width=300,
                    content=ft.TextField(
                        hint_text="Pesquisar cliente...",
                        prefix_icon=ft.Icons.SEARCH,
                    ),
                ),
            ],
        )

    def _painel_formulario(self):

        return ft.Container(
            expand=1,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            padding=20,
            shadow=ft.BoxShadow(
                blur_radius=8,
                spread_radius=1,
                color=ft.Colors.BLACK12,
            ),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Dados do Cliente",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Divider(),
                    ft.Text("O formulário será criado na próxima etapa."),
                    ft.Container(expand=True),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                "Guardar",
                                icon=ft.Icons.SAVE,
                                disabled=True,
                            ),
                            ft.OutlinedButton(
                                "Limpar",
                                icon=ft.Icons.CLEAR,
                                disabled=True,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def _painel_lista(self):

        return ft.Container(
            expand=2,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            padding=20,
            shadow=ft.BoxShadow(
                blur_radius=8,
                spread_radius=1,
                color=ft.Colors.BLACK12,
            ),
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Text(
                        "Lista de Clientes",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Divider(),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.Colors.GREY_100,
                        border_radius=8,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Text(
                            "A tabela será criada na próxima etapa.",
                            color=ft.Colors.GREY_700,
                        ),
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.OutlinedButton(
                                "Editar",
                                icon=ft.Icons.EDIT,
                                disabled=True,
                            ),
                            ft.OutlinedButton(
                                "Eliminar",
                                icon=ft.Icons.DELETE,
                                disabled=True,
                            ),
                            ft.ElevatedButton(
                                "Atualizar",
                                icon=ft.Icons.REFRESH,
                                disabled=True,
                            ),
                        ],
                    ),
                ],
            ),
        )