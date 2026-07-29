from src.database.conexao import conectar

def inserir(equipamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO equipamentos
        (id_cliente, tipo, marca, modelo, numero_serie, data_compra, observacoes)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (equipamento.id_cliente, equipamento.tipo, equipamento.marca, equipamento.modelo, equipamento.numero_serie, equipamento.data_compra, equipamento.observacoes)

    cursor.execute(sql, valores)
    conexao.commit()

    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()
    return equipamento


def listar():

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT
            id_equipamento,
            id_cliente,
            tipo,
            marca,
            modelo,
            numero_serie,
            data_compra,
            observacoes,
            status,
            created_at,
            updated_at,
            deleted_at
        FROM equipamentos
        WHERE status = 1
        ORDER BY marca, modelo
    """

    cursor.execute(sql)
    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamentos


def procurar_por_id(id_equipamento):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM equipamentos
        WHERE id_equipamento = %s
        AND status = 1
    """

    cursor.execute(sql, (id_equipamento,))
    equipamento = cursor.fetchone()

    cursor.close()
    conexao.close()
    return equipamento


def listar_por_cliente(id_cliente):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM equipamentos
        WHERE id_cliente = %s
        AND status = 1
        ORDER BY marca, modelo
    """

    cursor.execute(sql, (id_cliente,))
    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamentos


def procurar_por_numero_serie(numero_serie):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM equipamentos
        WHERE numero_serie = %s
        AND status = 1
    """

    cursor.execute(sql, (numero_serie,))
    equipamento = cursor.fetchone()

    cursor.close()
    conexao.close()
    return equipamento


def atualizar(equipamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamentos
        SET
            id_cliente = %s,
            tipo = %s,
            marca = %s,
            modelo = %s,
            numero_serie = %s,
            data_compra = %s,
            observacoes = %s,
            updated_at = NOW()
        WHERE id_equipamento = %s
        AND status = 1
    """

    valores = (equipamento.id_cliente, equipamento.tipo, equipamento.marca, equipamento.modelo, equipamento.numero_serie, equipamento.data_compra, equipamento.observacoes, equipamento.id_equipamento)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def excluir(id_equipamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamentos
        SET
            status = 0,
            deleted_at = NOW()
        WHERE id_equipamento = %s
        AND status = 1
    """

    cursor.execute(sql, (id_equipamento,))
    conexao.commit()

    cursor.close()
    conexao.close()


def restaurar(id_equipamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamentos

        SET

            status = 1,
            deleted_at = NULL,
            updated_at = NOW()

        WHERE id_equipamento = %s
    """

    cursor.execute(sql, (id_equipamento,))
    conexao.commit()

    cursor.close()
    conexao.close()


def contar():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT COUNT(*)

        FROM equipamentos

        WHERE status = 1
    """

    cursor.execute(sql)
    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()
    return total