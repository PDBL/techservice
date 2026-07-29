from src.views.menu_clientes import menu_clientes
from src.views.menu_equipamentos import menu_equipamentos
from src.views.menu_ordens import menu_ordens
from src.views.menu_historico import menu_historico
from src.utils.helpers import limpar_ecra, pausa

def menu_principal():

    while True:
        limpar_ecra()
        print("=" * 60)
        print("        TECHSERVICE")
        print("Sistema de Gestão de Assistência Técnica")
        print("=" * 60)
        print("\nMENU PRINCIPAL\n")
        print("1 - Clientes")
        print("2 - Equipamentos")
        print("3 - Ordens de Serviço")
        print("4 - Histórico")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_equipamentos()

        elif opcao == "3":
            menu_ordens()

        elif opcao == "4":
            menu_historico()

        elif opcao == "0":
            print("\nObrigado por utilizar o TechService.")
            break

        else:
            print("\nOpção inválida.")
            pausa()