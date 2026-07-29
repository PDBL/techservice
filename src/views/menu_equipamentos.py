from src.services.equipamento_service import *
from src.utils.helpers import pausa

def menu_equipamentos():

    while True:

        print("\n" * 30)

        print("=" * 60)
        print("MENU EQUIPAMENTOS")
        print("=" * 60)

        print("1 - Inserir Equipamento")
        print("2 - Listar Equipamentos")
        print("3 - Procurar por Número de Série")
        print("4 - Listar Equipamentos de um Cliente")
        print("5 - Atualizar Equipamento")
        print("6 - Desativar Equipamento")
        print("7 - Restaurar Equipamento")
        print("0 - Voltar")

        opcao = input("\nOpção: ")

        if opcao == "1":

            id_cliente = int(input("ID Cliente: "))
            tipo = input("Tipo: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            numero_serie = input("Número de Série: ")
            data_compra = input("Data Compra (AAAA-MM-DD): ")
            observacoes = input("Observações: ")

            inserir_equipamento(
                id_cliente,
                tipo,
                marca,
                modelo,
                numero_serie,
                data_compra,
                observacoes
            )

            print("\nEquipamento inserido com sucesso.")

            pausa()

        elif opcao == "2":

            equipamentos = listar_equipamentos()

            print()

            for equipamento in equipamentos:

                print(f"ID: {equipamento['id_equipamento']}")
                print(f"Cliente: {equipamento['id_cliente']}")
                print(f"Tipo: {equipamento['tipo']}")
                print(f"Marca: {equipamento['marca']}")
                print(f"Modelo: {equipamento['modelo']}")
                print(f"N.º Série: {equipamento['numero_serie']}")
                print(f"Data Compra: {equipamento['data_compra']}")
                print(f"Observações: {equipamento['observacoes']}")
                print("-" * 60)

            pausa()

        elif opcao == "3":

            numero = input("Número de Série: ")
            equipamento = procurar_numero_serie(numero)

            if equipamento:

                print()
                print(f"ID: {equipamento['id_equipamento']}")
                print(f"Marca: {equipamento['marca']}")
                print(f"Modelo: {equipamento['modelo']}")
                print(f"Cliente: {equipamento['id_cliente']}")

            else:

                print("\nEquipamento não encontrado.")

            pausa()

        elif opcao == "4":

            id_cliente = int(input("ID Cliente: "))
            equipamentos = listar_cliente(id_cliente)

            print()

            for equipamento in equipamentos:

                print(
                    equipamento["id_equipamento"],
                    equipamento["marca"],
                    equipamento["modelo"]
                )

            pausa()

        elif opcao == "5":

            id = int(input("ID Equipamento: "))
            equipamento = procurar_equipamento(id)

            if equipamento is None:

                print("\nEquipamento inexistente.")

                pausa()

                continue

            print("\nENTER mantém o valor atual.\n")

            id_cliente = input(
                f"ID Cliente ({equipamento['id_cliente']}): "
            ) or equipamento["id_cliente"]

            tipo = input(
                f"Tipo ({equipamento['tipo']}): "
            ) or equipamento["tipo"]

            marca = input(
                f"Marca ({equipamento['marca']}): "
            ) or equipamento["marca"]

            modelo = input(
                f"Modelo ({equipamento['modelo']}): "
            ) or equipamento["modelo"]

            numero = input(
                f"Número Série ({equipamento['numero_serie']}): "
            ) or equipamento["numero_serie"]

            data = input(
                f"Data Compra ({equipamento['data_compra']}): "
            ) or equipamento["data_compra"]

            observacoes = input(
                f"Observações ({equipamento['observacoes']}): "
            ) or equipamento["observacoes"]

            atualizar_equipamento(
                id,
                id_cliente,
                tipo,
                marca,
                modelo,
                numero,
                data,
                observacoes
            )

            print("\nEquipamento atualizado.")

            pausa()

        elif opcao == "6":

            id = int(input("ID Equipamento: "))

            desativar_equipamento(id)

            print("\nEquipamento desativado.")

            pausa()

        elif opcao == "7":

            id = int(input("ID Equipamento: "))

            restaurar_equipamento(id)

            print("\nEquipamento restaurado.")

            pausa()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida.")

            pausa()