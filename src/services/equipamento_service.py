from src.models.equipamento import Equipamento
from src.repositories import equipamento_repository

def inserir_equipamento(
    id_cliente,
    tipo,
    marca,
    modelo,
    numero_serie,
    data_compra,
    observacoes
):

    equipamento = Equipamento(
        id_cliente=id_cliente,
        tipo=tipo,
        marca=marca,
        modelo=modelo,
        numero_serie=numero_serie,
        data_compra=data_compra,
        observacoes=observacoes
    )

    return equipamento_repository.inserir(equipamento)

def listar_equipamentos():
    return equipamento_repository.listar()


def procurar_equipamento(id_equipamento):
    return equipamento_repository.procurar_por_id(id_equipamento)


def procurar_numero_serie(numero_serie):
    return equipamento_repository.procurar_por_numero_serie(numero_serie)


def listar_cliente(id_cliente):
    return equipamento_repository.listar_por_cliente(id_cliente)


def atualizar_equipamento(id_equipamento, id_cliente, tipo, marca, modelo, numero_serie, data_compra, observacoes):

    equipamento = Equipamento(
        id_equipamento=id_equipamento,
        id_cliente=id_cliente,
        tipo=tipo,
        marca=marca,
        modelo=modelo,
        numero_serie=numero_serie,
        data_compra=data_compra,
        observacoes=observacoes
    )

    equipamento_repository.atualizar(equipamento)


def desativar_equipamento(id_equipamento):
    equipamento_repository.excluir(id_equipamento)


def restaurar_equipamento(id_equipamento):
    equipamento_repository.restaurar(id_equipamento)


def contar_equipamentos():
    return equipamento_repository.contar()