def zerezima(conn):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tabela_votos') # apaga tudao da tabela voto
    cursor.execute('ALTER TABLE tabela_votos AUTO_INCREMENT = 1') 
    cursor.execute('UPDATE eleitores SET status_voto = 0 WHERE status_voto = 1')
    conn.commit()
    
    cursor.execute('''
        SELECT nome_completo, numero_votacao, nome_partido
        FROM candidatos
        ORDER BY nome_completo
    ''') # busca os cara
    
    candidatos = cursor.fetchall()

    print('\t\tzerézima\n')