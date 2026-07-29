from src.models.ordem_servico import OrdemServico
from src.services.ordem_servico_service import *
from src.utils.helpers import pausa

def menu_ordens():

    while True:

        print("\n" * 30)

        print("=" * 60)
        print(" MENU ORDENS DE SERVIÇO ")
        print("=" * 60)

        print("1 - Nova Ordem")
        print("2 - Listar Ordens")
        print("3 - Procurar Ordem")
        print("4 - Procurar por Equipamento")
        print("5 - Procurar por Estado")
        print("6 - Atualizar Ordem")
        print("7 - Alterar Estado")
        print("8 - Desativar Ordem")
        print("9 - Restaurar Ordem")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        if opcao == "1":

            id_equipamento = int(input("ID Equipamento: "))
            defeito = input("Defeito Relatado: ")
            diagnostico = input("Diagnóstico: ")
            solucao = input("Solução: ")
            estado = input("Estado: ")
            prioridade = input("Prioridade: ")
            valor_servico = float(input("Valor Serviço: "))
            valor_pecas = float(input("Valor Peças: "))
            desconto = float(input("Desconto: "))
            valor_total = float(input("Valor Total: "))
            observacoes = input("Observações: ")

            inserir_ordem(
                id_equipamento,
                defeito,
                diagnostico,
                solucao,
                estado,
                prioridade,
                valor_servico,
                valor_pecas,
                desconto,
                valor_total,
                observacoes
            )

            print("\nOrdem criada.")

            pausa()

        elif opcao == "2":

            ordens = listar_ordens()

            print()

            for ordem in ordens:

                print(
                    ordem["id_ordem"],
                    ordem["status_ordem"],
                    ordem["valor_total"]
                )

            pausa()

        elif opcao == "3":

            id_ordem = int(input("ID: "))

            ordem = procurar_ordem(id_ordem)

            print(ordem)

            pausa()

        elif opcao == "4":

            id_equipamento = int(input("ID Equipamento: "))

            ordens = listar_por_equipamento(id_equipamento)

            print()

            for ordem in ordens:

                print(ordem["id_ordem"], ordem["status_ordem"])

            pausa()

        elif opcao == "5":

            estado = input("Estado: ")

            ordens = listar_por_status(estado)

            print()

            for ordem in ordens:

                print(ordem["id_ordem"], ordem["status_ordem"])

            pausa()

        elif opcao == "6":

            print("\nA atualização completa será implementada na fase seguinte.")

            pausa()

        elif opcao == "7":

            id_ordem = int(input("ID: "))

            estado = input("Novo Estado: ")

            alterar_estado(id_ordem, estado)

            print("\nEstado alterado.")

            pausa()

        elif opcao == "8":

            id_ordem = int(input("ID: "))

            desativar_ordem(id_ordem)

            print("\nOrdem desativada.")

            pausa()

        elif opcao == "9":

            id_ordem = int(input("ID: "))

            restaurar_ordem(id_ordem)

            print("\nOrdem restaurada.")

            pausa()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida.")

            pausa()