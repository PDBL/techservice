from src.models.ordem_servico import OrdemServico
from src.repositories import ordem_servico_repository

def inserir_ordem(
        id_equipamento,
        defeito_relatado,
        diagnostico,
        solucao,
        status_ordem,
        prioridade,
        valor_servico,
        valor_pecas,
        desconto,
        valor_total,
        observacoes
):

    ordem = OrdemServico(
        id_equipamento=id_equipamento,
        defeito_relatado=defeito_relatado,
        diagnostico=diagnostico,
        solucao=solucao,
        status_ordem=status_ordem,
        prioridade=prioridade,
        valor_servico=valor_servico,
        valor_pecas=valor_pecas,
        desconto=desconto,
        valor_total=valor_total,
        observacoes=observacoes
    )

    return ordem_servico_repository.inserir(ordem)


def listar_ordens():
    return ordem_servico_repository.listar()


def procurar_ordem(id_ordem):
    return ordem_servico_repository.procurar_por_id(id_ordem)


def listar_por_equipamento(id_equipamento):
    return ordem_servico_repository.listar_por_equipamento(id_equipamento)


def listar_por_status(status):
    return ordem_servico_repository.listar_por_status(status)


def atualizar_ordem(ordem):
    ordem_servico_repository.atualizar(ordem)


def alterar_estado(id_ordem, estado):
    ordem_servico_repository.alterar_status(id_ordem, estado)


def desativar_ordem(id_ordem):
    ordem_servico_repository.excluir(id_ordem)


def restaurar_ordem(id_ordem):
    ordem_servico_repository.restaurar(id_ordem)