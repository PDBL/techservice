from src.database.conexao import conectar

def inserir(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes (nome, telefone, email, nif, morada)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (cliente.nome, cliente.telefone, cliente.email, cliente.nif, cliente.morada)

    cursor.execute(sql, valores)
    conexao.commit()
    cliente.id_cliente = cursor.lastrowid

    cursor.close()
    conexao.close()
    return cliente

def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_cliente, nome, telefone, email, nif,
            morada, status, created_at, updated_at, deleted_at
        FROM clientes
        WHERE status = 1
        ORDER BY nome
    """

    cursor.execute(sql)
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return clientes

def procurar_por_id(id_cliente):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM clientes
        WHERE id_cliente = %s
        AND status = 1
    """

    cursor.execute(sql, (id_cliente,))
    cliente = cursor.fetchone()

    cursor.close()
    conexao.close()
    return cliente


def procurar_por_nome(nome):

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM clientes
        WHERE nome LIKE %s
        AND status = 1
        ORDER BY nome
    """

    cursor.execute(sql, ("%" + nome + "%",))
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return clientes

def atualizar(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET nome = %s,
            telefone = %s,
            email = %s,
            nif = %s,
            morada = %s,
            updated_at = NOW()
        WHERE id_cliente = %s
          AND status = 1
    """
    valores = (cliente.nome, cliente.telefone, cliente.email, cliente.nif, cliente.morada, cliente.id_cliente)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def excluir(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET status = 0,
            deleted_at = NOW()
        WHERE id_cliente = %s
          AND status = 1
    """

    cursor.execute(sql, (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()

def contar():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT COUNT(*)
        FROM clientes
        WHERE status = 1
    """

    cursor.execute(sql)
    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()
    return total