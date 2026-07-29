from src.services.cliente_service import *
from src.utils.helpers import pausa

def menu_clientes():

    while True:
        print("\n" * 30)

        print("=" * 60)
        print("MENU CLIENTES")
        print("=" * 60)

        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Procurar por Nome")
        print("4 - Atualizar Cliente")
        print("5 - Desativar Cliente")
        print("6 - Restaurar Cliente")
        print("0 - Voltar")

        opcao = input("\nOpção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            nif = input("NIF: ")
            morada = input("Morada: ")

            inserir_cliente(nome, telefone, email, nif, morada)

            print("\nCliente inserido com sucesso.")

            pausa()

        elif opcao == "2":

            clientes = listar_clientes()

            print()

            for cliente in clientes:

                print(f"ID: {cliente['id_cliente']}")
                print(f"Nome: {cliente['nome']}")
                print(f"Telefone: {cliente['telefone']}")
                print(f"Email: {cliente['email']}")
                print(f"NIF: {cliente['nif']}")
                print(f"Morada: {cliente['morada']}")

                print("-" * 60)

            pausa()

        elif opcao == "3":

            nome = input("Nome: ")
            clientes = procurar_cliente_nome(nome)

            print()

            for cliente in clientes:

                print(cliente["id_cliente"], "-", cliente["nome"])

            pausa()

        elif opcao == "4":

            id_cliente = int(input("ID: "))
            cliente = procurar_cliente_id(id_cliente)

            if cliente is None:

                print("\nCliente inexistente.")

                pausa()

                continue

            print("\nENTER mantém o valor atual.\n")

            nome = input(f"Nome ({cliente['nome']}): ") or cliente["nome"]
            telefone = input(f"Telefone ({cliente['telefone']}): ") or cliente["telefone"]
            email = input(f"Email ({cliente['email']}): ") or cliente["email"]
            nif = input(f"NIF ({cliente['nif']}): ") or cliente["nif"]
            morada = input(f"Morada ({cliente['morada']}): ") or cliente["morada"]

            atualizar_cliente(id_cliente, nome, telefone, email, nif, morada)

            print("\nCliente atualizado.")

            pausa()

        elif opcao == "5":

            id_cliente = int(input("ID: "))

            desativar_cliente(id_cliente)

            print("\nCliente desativado.")

            pausa()

        elif opcao == "6":

            id_cliente = int(input("ID: "))

            restaurar_cliente(id_cliente)

            print("\nCliente restaurado.")

            pausa()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida.")

            pausa()