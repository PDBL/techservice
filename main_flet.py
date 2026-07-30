import flet as ft

from src.utils.theme import app_theme
from src.flet_views.cliente_view import ClienteView

def main(page: ft.Page):

    page.title = "TechService"

    page.theme = app_theme()
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window.width = 1400
    page.window.height = 850

    page.padding = 0

    page.bgcolor = ft.Colors.GREY_100

    area_trabalho = ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ClienteView(),
    )

    def selecionar_menu(e):

        indice = menu.selected_index

        if indice == 0:
            area_trabalho.content = ClienteView()

        else:
            area_trabalho.content = ft.Column(
                controls=[
                    ft.Text(
                        "Em desenvolvimento",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                    )
                ]
            )

        page.update()

    menu = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=90,
        min_extended_width=180,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON,
                label="Clientes",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.COMPUTER,
                label="Equipamentos",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.BUILD,
                label="Ordens",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.HISTORY,
                label="Histórico",
            ),
        ],
        on_change=selecionar_menu,
    )

    page.add(
        ft.Row(
            expand=True,
            controls=[
                menu,
                ft.VerticalDivider(width=1),
                area_trabalho,
            ],
        )
    )

ft.app(target=main)