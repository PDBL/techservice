from src.database.conexao import conectar

def inserir(ordem):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO ordens_servico
        (id_equipamento, defeito_relatado, diagnostico, solucao, status_ordem, prioridade, valor_servico, valor_pecas, desconto,valor_total,observacoes)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (ordem.id_equipamento, ordem.defeito_relatado, ordem.diagnostico, ordem.solucao, ordem.status_ordem, ordem.prioridade, ordem.valor_servico, ordem.valor_pecas, ordem.desconto, ordem.valor_total, ordem.observacoes)

    cursor.execute(sql, valores)
    conexao.commit()

    ordem.id_ordem = cursor.lastrowid

    cursor.close()
    conexao.close()
    return ordem


def listar():

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM ordens_servico
        WHERE status = 1
        ORDER BY data_abertura DESC
    """

    cursor.execute(sql)
    ordens = cursor.fetchall()

    cursor.close()
    conexao.close()
    return ordens


def procurar_por_id(id_ordem):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM ordens_servico
        WHERE id_ordem = %s
        AND status = 1
    """

    cursor.execute(sql, (id_ordem,))
    ordem = cursor.fetchone()

    cursor.close()
    conexao.close()
    return ordem


def listar_por_equipamento(id_equipamento):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM ordens_servico
        WHERE id_equipamento = %s
        AND status = 1
        ORDER BY data_abertura DESC
    """

    cursor.execute(sql, (id_equipamento,))
    ordens = cursor.fetchall()

    cursor.close()
    conexao.close()
    return ordens


def listar_por_status(status_ordem):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM ordens_servico
        WHERE status_ordem = %s
        AND status = 1
        ORDER BY data_abertura DESC
    """

    cursor.execute(sql, (status_ordem,))
    ordens = cursor.fetchall()

    cursor.close()
    conexao.close()
    return ordens


def atualizar(ordem):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordens_servico

        SET
            id_equipamento = %s,
            defeito_relatado = %s,
            diagnostico = %s,
            solucao = %s,
            status_ordem = %s,
            prioridade = %s,
            valor_servico = %s,
            valor_pecas = %s,
            desconto = %s,
            valor_total = %s,
            observacoes = %s,
            updated_at = NOW()
        WHERE id_ordem = %s
        AND status = 1
    """

    valores = (
        ordem.id_equipamento,
        ordem.defeito_relatado,
        ordem.diagnostico,
        ordem.solucao,
        ordem.status_ordem,
        ordem.prioridade,
        ordem.valor_servico,
        ordem.valor_pecas,
        ordem.desconto,
        ordem.valor_total,
        ordem.observacoes,
        ordem.id_ordem
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def alterar_status(id_ordem, novo_status):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordens_servico
        SET

            status_ordem = %s,
            updated_at = NOW()
        WHERE id_ordem = %s
        AND status = 1
    """

    cursor.execute(sql, (novo_status, id_ordem))
    conexao.commit()

    cursor.close()
    conexao.close()


def excluir(id_ordem):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordens_servico
        SET
            status = 0,
            deleted_at = NOW()
        WHERE id_ordem = %s
        AND status = 1
    """

    cursor.execute(sql, (id_ordem,))
    conexao.commit()

    cursor.close()
    conexao.close()


def restaurar(id_ordem):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE ordens_servico
        SET
            status = 1,
            deleted_at = NULL,
            updated_at = NOW()
        WHERE id_ordem = %s
    """

    cursor.execute(sql, (id_ordem,))
    conexao.commit()

    cursor.close()
    conexao.close()


def contar():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT COUNT(*)
        FROM ordens_servico
        WHERE status = 1
    """

    cursor.execute(sql)
    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()
    return total