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

        self.txt_id = ft.TextField(
            label="ID",
            read_only=True,
            disabled=True,
        )
        self.txt_nome = ft.TextField(
            label="Nome *",
            hint_text="Nome completo do cliente",
        )
        self.txt_email = ft.TextField(
            label="Email *",
            hint_text="email@exemplo.pt",
        )
        self.txt_telefone = ft.TextField(
            label="Telefone",
            hint_text="9xxxxxxxx",
        )
        self.txt_nif = ft.TextField(
            label="NIF",
            hint_text="123456789",
        )
        self.txt_morada = ft.TextField(
            label="Morada",
            multiline=True,
            min_lines=2,
            max_lines=3,
        )

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
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.PERSON,
                                color=ft.Colors.BLUE,
                            ),
                            ft.Text(
                                "Dados do Cliente",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                            )
                        ]
                    ),
                    ft.Divider(),
                    self.txt_id,
                    self.txt_nome,
                    self.txt_email,
                    self.txt_telefone,
                    self.txt_nif,
                    self.txt_morada,
                    ft.Container(expand=True),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(
                                "Guardar",
                                icon=ft.Icons.SAVE,
                                width=120,
                            ),
                            ft.OutlinedButton(
                                "Limpar",
                                icon=ft.Icons.CLEAR,
                                width=120,
                            )
                        ]
                    )
                ]
            )
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