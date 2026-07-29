from src.models.historico_ordem_servico import HistoricoOrdemServico
from src.repositories import historico_ordem_servico_repository

def inserir_historico(
    id_ordem,
    status_anterior,
    status_novo,
    observacao
):

    historico = HistoricoOrdemServico(
        id_ordem=id_ordem,
        status_anterior=status_anterior,
        status_novo=status_novo,
        observacao=observacao
    )

    return historico_ordem_servico_repository.inserir(historico)

def listar_historico():
    return historico_ordem_servico_repository.listar()

def listar_historico_ordem(id_ordem):
    return historico_ordem_servico_repository.listar_por_ordem(id_ordem)

def procurar_historico(id_historico):
    return historico_ordem_servico_repository.procurar_por_id(id_historico)

def desativar_historico(id_historico):
    historico_ordem_servico_repository.excluir(id_historico)

def restaurar_historico(id_historico):
    historico_ordem_servico_repository.restaurar(id_historico)

def contar_historico():
    return historico_ordem_servico_repository.contar()