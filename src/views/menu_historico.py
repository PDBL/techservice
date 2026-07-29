from src.services.historico_ordem_servico_service import *
from src.utils.helpers import pausa

def menu_historico():

    while True:

        print("\n" * 30)

        print("=" * 60)
        print("MENU HISTÓRICO")
        print("=" * 60)

        print("1 - Inserir Registo")
        print("2 - Listar Histórico")
        print("3 - Histórico de uma Ordem")
        print("4 - Procurar Registo")
        print("5 - Desativar Registo")
        print("6 - Restaurar Registo")
        print("0 - Voltar")

        opcao = input("\nOpção: ")

        if opcao == "1":

            id_ordem = int(input("ID Ordem: "))
            estado_anterior = input("Estado anterior: ")
            estado_novo = input("Novo estado: ")
            observacao = input("Observação: ")

            inserir_historico(
                id_ordem,
                estado_anterior,
                estado_novo,
                observacao
            )

            print("\nHistórico registado com sucesso.")

            pausa()

        elif opcao == "2":

            historico = listar_historico()

            print()

            for item in historico:

                print(f"ID...............: {item['id_historico']}")
                print(f"Ordem............: {item['id_ordem']}")
                print(f"Estado anterior..: {item['status_anterior']}")
                print(f"Estado novo......: {item['status_novo']}")
                print(f"Data.............: {item['data_alteracao']}")
                print("-" * 60)

            pausa()

        elif opcao == "3":

            id_ordem = int(input("ID Ordem: "))

            historico = listar_historico_ordem(id_ordem)

            print()

            for item in historico:

                print(
                    item["data_alteracao"],
                    item["status_anterior"],
                    "->",
                    item["status_novo"]
                )

            pausa()

        elif opcao == "4":

            id_historico = int(input("ID: "))

            item = procurar_historico(id_historico)

            if item:

                print()

                print(f"Ordem: {item['id_ordem']}")
                print(f"Anterior: {item['status_anterior']}")
                print(f"Novo: {item['status_novo']}")
                print(f"Observação: {item['observacao']}")

            else:

                print("\nRegisto não encontrado.")

            pausa()

        elif opcao == "5":

            id = int(input("ID: "))

            desativar_historico(id)

            print("\nRegisto desativado.")

            pausa()

        elif opcao == "6":

            id = int(input("ID: "))

            restaurar_historico(id)

            print("\nRegisto restaurado.")

            pausa()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida.")

            pausa()