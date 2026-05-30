import time


def zerezima(conn):
    """
    Esta função realiza a zerézima do sistema eleitoral, removendo todos os votos registrados, redefinindo o contador automático da tabela de votos 
    e atualizando o status dos eleitores, garantindo que o sistema esteja pronto para uma nova votação.

    Args:
        conn (mysql.connector): Conexão ativa com o banco de dados MySQL.

    Returns:
        None: A função não retorna valores, apenas executa operações no banco de dados e exibe o resultado da zerézima no console.
    """
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tabela_votos') # apaga tudao da tabela voto
    cursor.execute('ALTER TABLE tabela_votos AUTO_INCREMENT = 1') 
    cursor.execute('UPDATE eleitores SET status_voto = 0 WHERE status_voto = 1')
    conn.commit()
    print('APLICANDO ZERÉZIMA, AGUARDE...')
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print('')
    cursor.execute('''
        SELECT c.nome_completo, c.numero_votacao, c.nome_partido, COUNT(v.id_candidato) as total
        FROM candidatos c
        LEFT JOIN tabela_votos v ON c.id = v.id_candidato
        GROUP BY c.id
        ORDER BY total DESC
    ''') # busca os cara
    
    candidatos = cursor.fetchall()
    for i in candidatos:
        print(f'{i[1]} - {i[0]} ({i[2]}) --> {i[3]} votos')
        
    print('\t\tZerézima Aplicada\n')