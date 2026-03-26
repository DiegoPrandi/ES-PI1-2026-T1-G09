import os
from db import conexao
import ascii

"""
    Para fazer a conexão com o banco precisa inicialmente instalar a 
    biblioteca mysql.connector, so digitar no terminal
    pip install mysql-connector-python
    
    Depois cria na pasta raiz do projeto
    um arquivo .env com as seguintes informações
    
    DB_HOST=mysql-247ea64d-pi.b.aivencloud.com
    DB_PORT=15817
    DB_USER=coloca user aqui
    DB_PASSWORD=coloca pwd aqui
    DB_NAME=projeto_teste
    
    Só trocar os valores da USEr e PASSWORD para o certo
    Como é um repositorio publico e estamos usando um database remoto
    Por motivos de segurança usamos o .env para ocultar as informações
    De acesso ao banco, para somente a gente ter acesso.
"""
conexao = conexao()
cursor = conexao.cursor()


def gerenciamento():
    os.system('cls')
    
    ascii.gerenciamentoASCII()
    
    print('''
          1. Gestão de Eleitores
          2. Gestão de Candidatos
          3. Voltar
          ''')
    n = int(input('-> '))

    if n == 1:

        os.system('cls')

        def gestao_eleitores():

            print('''
                Digite o número da opção desejada:

                1. Cadastrar Eleitor
                2. Editar/Remover Eleitor
                3. Buscar Eleitor
                4. Listar Eleitores
                5. Voltar
            ''')

            n = int(input("-> "))

            if (n == 1):

                os.system('cls')

                def cadastrar_eleitor():
                    n = input("\nPressione ENTER para cadastrar um eleitor.")
                    print("\nEleitor cadastrado!\n")

                cadastrar_eleitor()

            elif (n == 2):

                os.system('cls')

                def editar_remover_eleitor():
                    n = input("\nPressione ENTER para editar/remover um eleitor.")
                    print("\nEleitor editado/removido!\n")

                editar_remover_eleitor()

            elif (n == 3):

                os.system('cls')

                def buscar_eleitor():
                    n = input("\nPressione ENTER para buscar eleitores.")
                    print("\nBuscando eleitores!\n")

                buscar_eleitor()

            elif (n == 4):

                os.system('cls')

                def listar_eleitores():
                    n = input("\nPressione ENTER para listar todos os eleitores.")
                    print('''
                        - Diego Prandi
                        - João Grisolia
                        - Matheus Ribeiro
                        - Rafael França
                        - Felipe Oliveira
                    ''')

                listar_eleitores()

            elif (n == 5):

                os.system('cls')
                gerenciamento()

            else:

                while True:

                    os.system('cls')
                    print("\nDigite alguma das opções válidas:\n")
                    n = int(input("-> "))

                    if (n == 1):
                        os.system('cls')
                        cadastrar_eleitor()
                    
                    elif (n == 2):
                        os.system('cls')
                        editar_remover_eleitor()

                    elif (n == 3):
                        os.system('cls')
                        buscar_eleitores()

                    elif (n == 4):
                        os.system('cls')
                        listar_eleitores()
                    
                    elif (n == 5):
                        os.system('cls')
                        gerenciamento()

        gestao_eleitores()

    elif n == 2:

        def gestao_candidatos():

            os.system('cls')
            print('''
            \nDigite o número da opção desejada.

            1. Cadastrar Candidato
            2. Editar Candidato
            3. Buscar Candidato
            4. Listar Candidatos
            5. Voltar
            ''')

            n = int(input("-> "))

            if (n == 1):
                def cadastrar_candidato():
                    os.system('cls')
                    name = str(input('Digite o nome do candidato: '))
                    number = int(input('Digite o número do candidato: '))
                    partido = str(input('Digite o partido do candidato: '))
                    
                    sql = 'INSERT INTO candidatos (nome_completo, numero_votacao, nome_partido) VALUES (%s, %s, %s)'
                    val = (name, number, partido)

                    cursor.execute(sql, val)
                    conexao.commit()
                    
                    print("\nCandidato cadastrado!\n")
                    input('Pressione ENTER para voltar ao menu.')
                    menu()
                cadastrar_candidato()


            elif (n == 2):

                os.system('cls')
                def editar_candidato():

                    nome = str(input("Digite o nome do candidato que deseja alterar: "))
                    sql = 'SELECT * FROM candidatos'
                    cursor.execute(sql)
                    result = cursor.fetchall()

                    if not result:
                        print("\nNenhum candidato encontrado.\n")
                        input("Pressione ENTER para voltar ao menu.")
                        menu()

                    for candidato in result:
                        if nome == candidato[1]:
                            name = str(input("Digite um novo nome para o candidato: "))
                            number = int(input("Digite o número do partido: "))
                            partido = str(input("Digite o nome do partido: "))

                            sql = 'UPDATE candidatos SET nome_completo=%s, numero_votacao=%s, nome_partido=%s WHERE id=%s'
                            values = (name, number, partido, candidato[0])

                            cursor.execute(sql, values)
                            conexao.commit()

                            print("\nCandidato alterado!")
                            input("\nPressione ENTER para voltar ao menu.")
                            menu()




                editar_candidato()

            elif (n == 3):

                os.system('cls')
                def buscar_candidato():
                    nome = str(input("\nDigite o nome do candidato: "))
                    sql = 'SELECT * FROM candidatos'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    
                    print("\nCandidatos encontrados:\n")
                    print('-' * 120)
                    for candidato in result:
                        if nome == candidato[1]:
                            print(f"Nome: {candidato[1]} | Número: {candidato[2]} | Partido: {candidato[3]}")
                    print('-' * 120)
                    input('\nPressione ENTER para voltar ao menu.')
                    menu()
                buscar_candidato()

            elif (n == 4):

                os.system('cls')
                def listar_candidatos():
                    sql = 'SELECT * FROM candidatos'
                    cursor.execute(sql)
                    result = cursor.fetchall()

                    print("\nCandidatos cadastrados:\n")
                    print('-' * 120)
                    for candidato in result:
                        print(f"Nome: {candidato[1]} | Número: {candidato[2]} | Partido: {candidato[3]}")
                    print('-' * 120)

                listar_candidatos()
                input('\nPressione ENTER para voltar ao menu.')
                input('')
                gestao_candidatos()

            elif (n == 5):

                os.system('cls')
                gerenciamento()

            else:

                while True:
                    
                    os.system('cls')
                    print("\nDigite alguma das opções válidas.\n")
                    n = int(input("-> "))

                    if (n == 1):
                        os.system('cls')
                        cadastrar_candidato()

                    if (n == 2):
                        os.system('cls')
                        editar_candidato()
                    
                    if (n == 3):
                        os.system('cls')
                        buscar_candidato()

                    if (n == 4):
                        os.system('cls')
                        listar_candidatos()

                    if (n == 5):
                        os.system('cls')
                        gerenciamento()

        gestao_candidatos()


    elif n == 3:
        menu()

def votacao():
    os.system('cls')
    ascii.votacaoASCII()

    n = input("\nPressione ENTER para abrir o mesário.\n")
    mesario()

def mesario():
    os.system('cls')
    ascii.mesarioASCII()

    print('''
        Digite o valor da opção desejada:

        1. Menu da Urna
        2. Resultados
        3. Auditoria
        4. Voltar
    ''')
    n = int(input("-> "))

    if (n == 1):
        def menu_urna():
            os.system('cls')

            print('''
                    Menu da Urna

                    1. Votar
                    2. Encerrar
            
                ''')

            n = int(input("-> "))

            if (n == 1):
                print("Você votou!")

            elif (n == 2):
                print("Sistema encerrado.")

            else:

                while True:
                    print("\nDigite uma opção válida.\n")
                    n = int(input("-> "))

                    if (n == 1):
                        print("Você votou!")
                        break

                    elif (n == 2):
                        print("\nSistema encerrado.\n")
                        break
                

        menu_urna()
    
    elif (n == 2):
        def resultados_votacao():
            os.system('cls')

            print('''
                Resultados

                1. Boletim de Urna
                2. Estatísticas
                3. Votos por Partido
            
            ''')

            n = int(input("-> "))

        resultados_votacao()

    elif (n == 3):
        def auditoria_votacao():
            os.system('cls')

            print('''
                Auditoria

                1. Ver Logs
                2. Ver Protocolos
            
            ''')

            n = int(input("-> "))

        auditoria_votacao()
    
    elif (n == 4):
        os.system('cls')
        menu()

def menu():
    os.system('cls')
    ascii.menuASCII()
    print('BEM VINDO A VOTACAO')
    
    print('''
            Digite a opção que deseja realizar: 

            1. Gerenciamento
            2. Votação
            3. Sair
        ''')
    n = int(input('-> '))

    if n == 1:
        gerenciamento()
    elif n == 2:
        votacao()
    elif n == 3:
        print('\nSistema encerrado.\n')
        
    else:   
        while True: 
            print('\nDigite alguma das opções válidas.\n')
            n = int(input('-> '))
            
            if n == 1:
                os.system('cls')
                gerenciamento()
                
            elif n == 2:
                os.system('cls')    
                votacao()
            
            elif n == 3:
                print('\nSistema encerrado.\n')
                break

menu()