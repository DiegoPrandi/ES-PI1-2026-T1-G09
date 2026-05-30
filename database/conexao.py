import mysql.connector

def conectar():
    """
    Esta função realiza o processo de fazer a conexão do programa com o banco de dados.

    Args:
        None.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexão com o banco de dados caso a conexão seja bem-sucedida.
        None: Retornado caso ocorra erro na conexão com o banco de dados.

    """
    try: # tenta fazer a conexão com o banco
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            port=3306,
            password='root123@',
            database='projetopi',
        )

        return conexao # se der tudo certinho retorna a conexão

    except mysql.connector.Error as erro: # se a conexao der erro
        print("Erro ao conectar no banco:", erro) # printa o erro
        return None  # retorna nada pq deu erro 
