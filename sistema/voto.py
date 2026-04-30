import random
import string
from funcoes.criptografia import criptografia
from funcoes.validacaoCPF import validar_cpf, limpar_cpf
import mysql.connector
from datetime import datetime


'''
    menu -> votacao - > voto.py
    aqui tem que implementar a parte de votar
    pedir pro eleitor realizar o login 
    validar no banco a senha, ver se ja votou, cpf e valido...
'''

def login(conn):
    try:
        cursor = conn.cursor() # Cria um cursor pra fazer as mudanças

        cpf = str(input("Digite seu CPF: "))
        while not validar_cpf(cpf):
                        print("CPF inválido. Tente novamente.")
                        cpf = str(input("Digite seu CPF: "))
        cpf = limpar_cpf(cpf)
        cpf = criptografia(cpf) # Criptografa o cpf

        titulo = str(input("Digite seu título de eleitor: "))

        chave = str(input("Digite a chave de acesso: "))
        chave = criptografia(chave) # Criptografa a chave

        cursor.execute('''
            SELECT id FROM eleitores WHERE cpf_criptografado = %s AND chave_acesso = %s AND titulo_eleitor = %s
                     ''', (cpf, chave, titulo)) # Aqui basicamente o cursor executa um comando que seleciona o id do eleitor onde há o cpf e chave de acesso iguais

        resultado = cursor.fetchone() # Guarda o resultado do cursor em uma variável

        if resultado: # Se o resultado existir
            id_eleitor = resultado[0] # Acessa o resultado anterior que era uma tupla em valor inteiro e guarda na variável id_eleitor
            return id_eleitor # Retorna o id do eleitor 
        else:
            print("CPF, TÍTULO ou CHAVE inválidos. Tente novamente.") # Se retornar nada, significa que o CPF, TÍTULO ou CHAVE estão invalidas
            return login(conn) # Retorna pra função novamente

    except ValueError:
        print("Erro. Tente novamente.")
        return login(conn) # Em caso de erro, retorna pra função novamente
    
    finally: # Quando tudo acima terminar
        cursor.close() # Fecha o cursor

def verificar_voto(eleitor_id, conn): # Criação de uma função com um parâmetro

    try:
        cursor = conn.cursor() # Criação do cursor para modificação do banco

        cursor.execute('''
            SELECT status_voto FROM eleitores WHERE id = %s
                       ''',(eleitor_id,)) # Seleciona o status do voto do eleitor em base de seu id
        
        voto_status = cursor.fetchone()[0] # Extrai o valor que está dentro da tupla para dentro da variável voto_status

        return voto_status # Retorna o status do voto

    except  mysql.connector.Error as e: # Tratando erros 
        print(f"Erro no banco: {e}")
                        
    finally: # Quando tudo acima tiver feito fecha o cursor e a conexão com o banco
        cursor.close()

def adicionar_voto(eleitor_id, conn): # Criação de uma função com um parâmetro do id do eleitor

    try:
        cursor = conn.cursor() # Cria um cursor para modificação no banco
        voto = int(input("Digite o número de seu candidato: "))

        sql = 'SELECT nome_completo, numero_votacao, nome_partido FROM candidatos WHERE numero_votacao = %s'
        cursor.execute(sql,(voto,))

        resultado = cursor.fetchone()
        if resultado:
            print(f"Nome: {resultado[0]}")
            print(f"Número: {resultado[1]}")
            print(f"Partido: {resultado[2]}")

        n = str(input("Deseja confirmar seu voto no seguinte candidato? (S/N) ->")).lower()

        while n != "s" and n != "n":

            if (n == "s"):
                
                cursor.execute('''
                    SELECT id FROM candidatos WHERE numero_votacao = %s
                            ''', (voto,)) # Seleciona o id do candidato em base do seu numero de voto
                id_candidato = cursor.fetchone() # Atribui ao id_candidato a tupla 

                if id_candidato: # Se a tupla id_candidato existir, ou seja, se o número do candidato for válido, extrai o valor do id do candidato da tupla e atribui à variável id_candidato
                    id_candidato = id_candidato[0] # Extrai o valor id do candidato da tupla
                else:
                    id_candidato = None #None será salvo como NULL no banco de dados. 
                
                data_atual = datetime.now() # Pega a data atual

                #Criação do protocolo de votação
                letra1 = random.choice(string.ascii_uppercase) # Gera uma letra maiúscula aleatória
                letra2 = random.choice(string.ascii_uppercase) # Gera uma letra maiúscula aleatória
                num1 = random.choice (string.digits) # Gera um número aleatório
                num2 = random.choice (string.digits) # Gera um número aleatório
                num3 = random.choice (string.digits) # Gera um número aleatório
                num4 = random.choice (string.digits) # Gera um número aleatório
                num5 = random.choice (string.digits) # Gera um número aleatório

                ano = "26" # Define o ano como 2026
                numero_candidato = str(voto) # Converte o número do candidato para string   

                protocolo = (
                    "V" +
                    letra1 +
                    letra2 +
                    ano +
                    numero_candidato +
                    num1 +
                    num2 +
                    num3 +
                    num4 +
                    num5
                        ) # Cria o protocolo de votação juntando as partes  
                
                protocolo_criptografado = criptografia(protocolo)
                
                cursor.execute('''
                    INSERT into tabela_votos (id_candidato, data_hora_voto, protocolo_criptografado)
                    VALUES (%s, %s, %s)
                            ''', (id_candidato, data_atual, protocolo_criptografado)) # Insere no banco as informações de votação
                
                conn.commit() # Comita tudo

                print("Voto registrado com sucesso!")
                print("Protocolo de votação:", protocolo) # Mostra o protocolo de votação para o eleitor

                # busca os dados do candidato votado
                if id_candidato != None:
                    cursor.execute('''
                        SELECT nome_completo, numero_votacao, nome_partido 
                        FROM candidatos 
                        WHERE id = %s
                    ''', (id_candidato,))
                    candidato = cursor.fetchone()

                    if candidato:
                        print(f"| Nome: {candidato[0]}", f"Número: {candidato[1]} |", f"Partido: {candidato[2]} |")

                cursor.execute('''
                    UPDATE eleitores SET status_voto = %s WHERE id = %s
                            ''', (1, eleitor_id)) # Da update no status do eleitor
                conn.commit() # Comita

            elif (n == "n"):
                n = input("Seu voto não será computado. Pressione ENTER para voltar.")
                return None

                from menu.votacao import menu_urna
                menu_urna(conn)
        
    except mysql.connector.IntegrityError as e:
        print(f"\nErro ao votar: {e}") # Mostrando algum erro

    finally:
        cursor.close() # Fecha o cursor
