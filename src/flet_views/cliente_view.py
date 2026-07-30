import flet as ft

from src.services import cliente_service

class ClienteView(ft.Container):

    def __init__(self):

        super().__init__()

        self.expand = True
        self.padding = 20

        self.cliente_selecionado = None

        self.txt_id = ft.TextField(
            label="ID",
            disabled=True,
            read_only=True,
        )

        self.txt_nome = ft.TextField(
            label="Nome *",
            hint_text="Nome completo",
        )

        self.txt_email = ft.TextField(
            label="Email *",
            hint_text="email@empresa.pt",
        )

        self.txt_telefone = ft.TextField(
            label="Telefone",
        )

        self.txt_nif = ft.TextField(
            label="NIF",
        )

        self.txt_morada = ft.TextField(
            label="Morada",
            multiline=True,
            min_lines=2,
            max_lines=3,
        )

        self.txt_pesquisa = ft.TextField(
            hint_text="Pesquisar cliente...",
            prefix_icon=ft.Icons.SEARCH,
            width=320,
        )

        self.btn_novo = ft.FilledButton(
            "Novo",
            icon=ft.Icons.ADD,
        )

        self.btn_guardar = ft.FilledButton(
            "Guardar",
            icon=ft.Icons.SAVE,
        )

        self.btn_limpar = ft.OutlinedButton(
            "Limpar",
            icon=ft.Icons.CLEAR,
        )

        self.btn_editar = ft.OutlinedButton(
            "Editar",
            icon=ft.Icons.EDIT,
            disabled=True,
        )

        self.btn_desativar = ft.OutlinedButton(
            "Desativar",
            icon=ft.Icons.DELETE,
            disabled=True,
        )

        self.btn_restaurar = ft.OutlinedButton(
            "Restaurar",
            icon=ft.Icons.RESTORE,
            disabled=True,
        )

        self.btn_atualizar = ft.IconButton(
            icon=ft.Icons.REFRESH,
            tooltip="Atualizar lista",
        )

        self.btn_novo.on_click = self.novo_cliente
        self.btn_limpar.on_click = self.limpar_formulario
        self.btn_atualizar.on_click = self.atualizar_tabela
        self.txt_pesquisa.on_change = self.pesquisar
        self.btn_guardar.on_click = self.guardar_cliente
        self.btn_editar.on_click = self.editar_cliente
        self.btn_desativar.on_click = self.desativar_cliente
        self.btn_restaurar.on_click = self.restaurar_cliente

        self.tabela = ft.DataTable(
            expand=True,
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Email")),
                ft.DataColumn(ft.Text("Telefone")),
            ],
            rows=[],
        )

        self.content = ft.Column(
            expand=True,
            spacing=15,
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

        self.carregar_clientes()

    def _cabecalho(self):

        return ft.Row(

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
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

                ft.Row(
                    spacing=10,
                    controls=[

                        self.txt_pesquisa,
                        self.btn_atualizar,
                        self.btn_novo,
                    ],
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

                expand=True,
                scroll=ft.ScrollMode.AUTO,
                controls=[

                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.PERSON,
                                color=ft.Colors.BLUE,
                                size=28,
                            ),

                            ft.Text(
                                "Dados do Cliente",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
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
                        spacing=10,
                        controls=[
                            self.btn_guardar,
                            self.btn_editar,
                        ],
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            self.btn_desativar,
                            self.btn_restaurar,
                            self.btn_limpar,
                        ],
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
                        padding=10,
                        content=self.tabela,
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            self.btn_editar,
                            self.btn_desativar,
                            self.btn_restaurar,
                        ],
                    ),
                ],
            ),
        )

    def carregar_clientes(self):

        self.tabela.rows.clear()

        try:

            clientes = cliente_service.listar_clientes()

            for cliente in clientes:

                self.tabela.rows.append(
                    ft.DataRow(
                        on_select_change=lambda e, c=cliente: self.selecionar_cliente(c),
                        cells=[
                            ft.DataCell(
                                ft.Text(str(cliente["id_cliente"]))
                            ),
                            ft.DataCell(
                                ft.Text(cliente["nome"])
                            ),
                            ft.DataCell(
                                ft.Text(cliente["email"])
                            ),
                            ft.DataCell(
                                ft.Text(cliente["telefone"] or "")
                            ),
                        ],
                    )
                )

        except Exception as erro:

            print(f"Erro ao carregar clientes: {erro}")

    def atualizar_tabela(self, e=None):

        self.carregar_clientes()

        self.update()

    def limpar_formulario(self, e=None):

        self.txt_id.value = ""
        self.txt_nome.value = ""
        self.txt_email.value = ""
        self.txt_telefone.value = ""
        self.txt_nif.value = ""
        self.txt_morada.value = ""
        self.cliente_selecionado = None
        self.btn_guardar.disabled = False
        self.btn_editar.disabled = True
        self.btn_desativar.disabled = True
        self.btn_restaurar.disabled = True

        self.update()

    def novo_cliente(self, e=None):

        self.cliente_selecionado = None
        self.limpar_formulario()
        self.txt_nome.focus()
        
        self.update()

    def pesquisar(self, e):

        pass

    def mostrar_mensagem(self, mensagem, cor=ft.Colors.GREEN):

        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                "Informação",
                color=cor,
                weight=ft.FontWeight.BOLD,
            ),
            content=ft.Text(mensagem),
            actions=[
                ft.TextButton(
                    "OK",
                    on_click=lambda e: self.page.pop_dialog(),
                )
            ],
        )

        self.page.show_dialog(dialogo)

    def guardar_cliente(self, e=None):

        try:

            cliente_service.inserir_cliente(

                nome=self.txt_nome.value,
                telefone=self.txt_telefone.value,
                email=self.txt_email.value,
                nif=self.txt_nif.value,
                morada=self.txt_morada.value,
            )

            self.carregar_clientes()
            self.limpar_formulario()
            self.mostrar_mensagem(
                "Cliente gravado com sucesso!"
            )

        except Exception as erro:

            self.mostrar_mensagem(
                str(erro),
                ft.Colors.RED,
            )

    def editar_cliente(self, e=None):

        print("Editar cliente")

    def desativar_cliente(self, e=None):

        print("Desativar cliente")

    def restaurar_cliente(self, e=None):

        print("Restaurar cliente")

    def selecionar_cliente(self, cliente):

        self.cliente_selecionado = cliente

        self.txt_id.value = str(cliente["id_cliente"])
        self.txt_nome.value = cliente["nome"]
        self.txt_email.value = cliente["email"]
        self.txt_telefone.value = cliente["telefone"] or ""
        self.txt_nif.value = cliente["nif"] or ""
        self.txt_morada.value = cliente["morada"] or ""

        self.btn_editar.disabled = False
        self.btn_desativar.disabled = False
        self.btn_restaurar.disabled = True

        self.update()