from src.models.cliente import Cliente
from src.repositories import cliente_repository
from src.utils.validacoes import validar_texto_obrigatorio

def inserir_cliente(nome, telefone, email, nif, morada):

    validar_texto_obrigatorio(nome, "Nome")
    validar_texto_obrigatorio(email, "Email")

    cliente = Cliente(nome=nome, telefone=telefone, email=email, nif=nif, morada=morada)

    return cliente_repository.inserir(cliente)


def listar_clientes():

    return cliente_repository.listar()

def listar_clientes_inativos():

    return cliente_repository.listar_inativos()


def procurar_cliente_id(id_cliente):

    return cliente_repository.procurar_por_id(id_cliente)


def procurar_cliente_nome(nome):

    return cliente_repository.procurar_por_nome(nome)


def atualizar_cliente(id_cliente, nome, telefone, email, nif, morada):

    cliente = Cliente(id_cliente=id_cliente, nome=nome, telefone=telefone, email=email, nif=nif, morada=morada)

    cliente_repository.atualizar(cliente)


def desativar_cliente(id_cliente):

    cliente_repository.excluir(id_cliente)


def restaurar_cliente(id_cliente):

    cliente_repository.restaurar(id_cliente)


def contar_clientes():

    return cliente_repository.contar()