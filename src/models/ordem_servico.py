class OrdemServico:

    def __init__(
        self,
        id_equipamento,
        defeito_relatado,
        diagnostico="",
        solucao="",
        status_ordem="ABERTA",
        prioridade="MEDIA",
        valor_servico=0.00,
        valor_pecas=0.00,
        desconto=0.00,
        valor_total=0.00,
        observacoes="",
        id_ordem=None,
        status=1
    ):
        self.id_ordem = id_ordem
        self.id_equipamento = id_equipamento
        self.defeito_relatado = defeito_relatado
        self.diagnostico = diagnostico
        self.solucao = solucao
        self.status_ordem = status_ordem
        self.prioridade = prioridade
        self.valor_servico = valor_servico
        self.valor_pecas = valor_pecas
        self.desconto = desconto
        self.valor_total = valor_total
        self.observacoes = observacoes
        self.status = status