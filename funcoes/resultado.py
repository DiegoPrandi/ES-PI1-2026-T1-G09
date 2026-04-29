import mysql.connector

def boletim_urna(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.nome, c.numero_votacao, c.partido, COUNT(v.id_candidato) as total
        FROM candidatos c
        LEFT JOIN tabela_votos v ON c.id = v.id_candidato
        GROUP BY c.id
        ORDER BY c.nome ASC
    """)

    resultados = cursor.fetchall()

    print("\n--- BOLETIM DE URNA ---")
    for nome, numero, partido, total in resultados:
        print(f"{nome} | Nº {numero} | {partido} | Votos: {total}")

    # vencedor
    cursor.execute("""
        SELECT c.nome, c.numero_votacao, c.partido, COUNT(v.id_candidato) as total
        FROM candidatos c
        LEFT JOIN tabela_votos v ON c.id = v.id_candidato
        GROUP BY c.id
        ORDER BY total DESC
        LIMIT 1
    """)

    vencedor = cursor.fetchone()

    if vencedor:
        print("\n--- VENCEDOR ---")
        print(f"Nome: {vencedor[0]}")
        print(f"Número: {vencedor[1]}")
        print(f"Partido: {vencedor[2]}")
        print(f"Votos: {vencedor[3]}")

    cursor.close()


def estatistica_comparecimento(conn):
    cursor = conn.cursor()

    # total de eleitores
    cursor.execute("SELECT COUNT(*) FROM eleitores")
    total_eleitores = cursor.fetchone()[0]

    # quem votou
    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 1")
    votaram = cursor.fetchone()[0]

    if total_eleitores > 0:
        percentual = (votaram / total_eleitores) * 100
    else:
        percentual = 0

    print("\n--- ESTATÍSTICA DE COMPARECIMENTO ---")
    print(f"Total de eleitores: {total_eleitores}")
    print(f"Votaram: {votaram}")
    print(f"Percentual: {percentual:.2f}%")

    cursor.close()


def votos_por_partido(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.partido, COUNT(v.id_candidato) as total
        FROM candidatos c
        LEFT JOIN tabela_votos v ON c.id = v.id_candidato
        GROUP BY c.partido
    """)

    resultados = cursor.fetchall()

    print("\n--- VOTOS POR PARTIDO ---")
    for partido, total in resultados:
        print(f"{partido}: {total} votos")

    cursor.close()


def validacao_integridade(conn):
    cursor = conn.cursor()

    # total de votos
    cursor.execute("SELECT COUNT(*) FROM tabela_votos")
    total_votos = cursor.fetchone()[0]

    # eleitores que votaram
    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE status_voto = 1")
    total_eleitor_voto = cursor.fetchone()[0]

    print("\n--- VALIDAÇÃO DE INTEGRIDADE ---")

    if total_votos == total_eleitor_voto:
        print("Integridade OK")
    else:
        print("Erro de integridade")
        print(f"Votos registrados: {total_votos}")
        print(f"Eleitores que votaram: {total_eleitor_voto}")

    cursor.close()