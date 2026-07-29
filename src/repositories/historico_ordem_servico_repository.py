from src.database.conexao import conectar

def inserir(historico):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO historico_ordens_servico
        (id_ordem, status_anterior, status_novo, observacao)
        VALUES
        (%s, %s, %s, %s)
    """

    valores = (historico.id_ordem, historico.status_anterior, historico.status_novo, historico.observacao)

    cursor.execute(sql, valores)
    conexao.commit()

    historico.id_historico = cursor.lastrowid

    cursor.close()
    conexao.close()
    return historico


def listar():

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM historico_ordens_servico
        WHERE status = 1
        ORDER BY data_alteracao DESC
    """

    cursor.execute(sql)
    historico = cursor.fetchall()

    cursor.close()
    conexao.close()
    return historico


def procurar_por_id(id_historico):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM historico_ordens_servico
        WHERE id_historico = %s
        AND status = 1
    """

    cursor.execute(sql, (id_historico,))
    historico = cursor.fetchone()

    cursor.close()
    conexao.close()
    return historico


def listar_por_ordem(id_ordem):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM historico_ordens_servico
        WHERE id_ordem = %s
        AND status = 1
        ORDER BY data_alteracao
    """

    cursor.execute(sql, (id_ordem,))
    historico = cursor.fetchall()

    cursor.close()
    conexao.close()
    return historico


def atualizar(historico):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE historico_ordens_servico
        SET
            id_ordem = %s,
            status_anterior = %s,
            status_novo = %s,
            observacao = %s,
            updated_at = NOW()
        WHERE id_historico = %s
        AND status = 1
    """

    valores = (
        historico.id_ordem,
        historico.status_anterior,
        historico.status_novo,
        historico.observacao,
        historico.id_historico
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def excluir(id_historico):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE historico_ordens_servico
        SET
            status = 0,
            deleted_at = NOW()
        WHERE id_historico = %s
        AND status = 1
    """

    cursor.execute(sql, (id_historico,))
    conexao.commit()

    cursor.close()
    conexao.close()


def restaurar(id_historico):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE historico_ordens_servico
        SET
            status = 1,
            deleted_at = NULL,
            updated_at = NOW()
        WHERE id_historico = %s
    """

    cursor.execute(sql, (id_historico,))
    conexao.commit()

    cursor.close()
    conexao.close()


def contar():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT COUNT(*)
        FROM historico_ordens_servico
        WHERE status = 1
    """

    cursor.execute(sql)
    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()
    return total