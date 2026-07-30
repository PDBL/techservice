import flet as ft

from src.flet_views.cliente_view import ClienteView
from src.flet_views.equipamento_view import EquipamentoView
from src.flet_views.ordem_view import OrdemView
from src.flet_views.historico_view import HistoricoView

def main(page: ft.Page):

    page.title = "TechService"
    page.window.width = 1400
    page.window.height = 800
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_100
    page.window.center()

    conteudo = ft.Container(
        expand=True
    )

    def mudar_pagina(e):

        indice = e.control.selected_index

        if indice == 0:
            conteudo.content = ClienteView(page)

        elif indice == 1:
            conteudo.content = EquipamentoView(page)

        elif indice == 2:
            conteudo.content = OrdemView(page)

        elif indice == 3:
            conteudo.content = HistoricoView(page)

        page.update()

    navigation = ft.NavigationRail(

        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=90,
        min_extended_width=200,

        leading=ft.Icon(
            ft.Icons.COMPUTER,
            size=40
        ),

        destinations=[

            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON,
                label="Clientes"
            ),

            ft.NavigationRailDestination(
                icon=ft.Icons.LAPTOP,
                label="Equipamentos"
            ),

            ft.NavigationRailDestination(
                icon=ft.Icons.BUILD,
                label="Ordens"
            ),

            ft.NavigationRailDestination(
                icon=ft.Icons.HISTORY,
                label="Histórico"
            ),
        ],
        on_change=mudar_pagina
    )

    conteudo.content = ClienteView(page)

    page.add(
        ft.Row(
            [
                navigation,
                ft.VerticalDivider(width=1),
                conteudo
            ],
            expand=True
        )
    )

ft.app(target=main)