class HistoricoOrdemServico:

    def __init__(
        self,
        id_ordem,
        status_novo,
        status_anterior="",
        observacao="",
        id_historico=None,
        status=1
    ):
        self.id_historico = id_historico
        self.id_ordem = id_ordem
        self.status_anterior = status_anterior
        self.status_novo = status_novo
        self.observacao = observacao
        self.status = status