import mysql.connector

def boletim_urna(conn):  # funcao que gera o boletim com os votos de todos os candidatos
    cursor = conn.cursor() 

    # consulta que busca todos os candidatos com seus respectivos votos (inclusive quem não recebeu votos)
    cursor.execute("""
        SELECT c.nome, c.numero_votacao, c.partido, COUNT(v.id_candidato) as total
        FROM candidatos c
        LEFT JOIN tabela_votos v ON c.id = v.id_candidato
        GROUP BY c.id
        ORDER BY c.nome ASC
    """)

    resultados = cursor.fetchall()  # armazena todos os resultados da consulta

    # percorre os resultados e exibe o boletim de urna formatado
    print("\n--- BOLETIM DE URNA ---")
    for nome, numero, partido, total in resultados:
        print(f"{nome} | Nº {numero} | {partido} | Votos: {total}")

    # consulta para obter apenas o candidato com maior número de votos (vencedor)
    cursor.execute("""
        SELECT c.nome, c.numero_votacao, c.partido, COUNT(v.id_candidato) as total
        FROM candidatos c
        LEFT JOIN tabela_votos v ON c.id = v.id_candidato
        GROUP BY c.id
        ORDER BY total DESC
        LIMIT 1
    """)

    vencedor = cursor.fetchone()  # pega apenas um resultado (o mais votado)

    # verifica se existe um vencedor e exibe seus dados
    if vencedor:
        print("\n--- VENCEDOR ---")
        print(f"Nome: {vencedor[0]}")
        print(f"Número: {vencedor[1]}")
        print(f"Partido: {vencedor[2]}")
        print(f"Votos: {vencedor[3]}")

    cursor.close()  # encerra o cursor


def estatistica_comparecimento(conn):  # funcao que calcula estatísticas de comparecimento dos eleitores
    cursor = conn.cursor()

    # busca o total de eleitores cadastrados
    cursor.execute("SELECT COUNT(*) FROM eleitores")
    total_eleitores = cursor.fetchone()[0]

    # busca quantos eleitores votaram (status_voto = 1)
    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 1")
    votaram = cursor.fetchone()[0]

    # calcula o percentual de comparecimento (evitando divisão por zero)
    if total_eleitores > 0:
        percentual = (votaram / total_eleitores) * 100
    else:
        percentual = 0

    # exibe os dados de comparecimento
    print("\n--- ESTATÍSTICA DE COMPARECIMENTO ---")
    print(f"Total de eleitores: {total_eleitores}")
    print(f"Votaram: {votaram}")
    print(f"Percentual: {percentual:.2f}%")

    cursor.close()


def votos_por_partido(conn):  # funcao que mostra a quantidade total de votos agrupados por partido
    cursor = conn.cursor()

    # consulta que agrupa os votos por partido
    cursor.execute("""
        SELECT c.partido, COUNT(v.id_candidato) as total
        FROM candidatos c
        LEFT JOIN tabela_votos v ON c.id = v.id_candidato
        GROUP BY c.partido
    """)

    resultados = cursor.fetchall()

    # percorre os resultados e exibe votos por partido
    print("\n--- VOTOS POR PARTIDO ---")
    for partido, total in resultados:
        print(f"{partido}: {total} votos")

    cursor.close()


def validacao_integridade(conn):  # funcao que verifica se a quantidade de votos bate com a quantidade de eleitores que votaram
    cursor = conn.cursor()

    # busca o total de votos registrados no sistema
    cursor.execute("SELECT COUNT(*) FROM tabela_votos")
    total_votos = cursor.fetchone()[0]

    # busca o total de eleitores que marcaram que votaram
    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 1")
    total_eleitor_voto = cursor.fetchone()[0]

    print("\n--- VALIDAÇÃO DE INTEGRIDADE ---")

    # compara os valores para verificar consistência dos dados
    if total_votos == total_eleitor_voto:
        print("Integridade OK")
    else:
        print("Erro de integridade")
        print(f"Votos registrados: {total_votos}")
        print(f"Eleitores que votaram: {total_eleitor_voto}")

    cursor.close()