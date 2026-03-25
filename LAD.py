import os
#import mysql.connector

def gerenciamento():
    os.system('cls')
    print('''                                                                                                  
 ,----.                                      ,--.                                   ,--.          
'  .-./    ,---. ,--.--. ,---. ,--,--,  ,---.`--' ,--,--.,--,--,--. ,---. ,--,--, ,-'  '-. ,---.  
|  | .---.| .-. :|  .--'| .-. :|      \| .--',--.' ,-.  ||        || .-. :|      |'-.  .-'| .-. | 
'  '--'  |\   --.|  |   \   --.|  ||  |\ `--.|  |\ '-'  ||  |  |  |\   --.|  ||  |  |  |  ' '-' ' 
 `------'  `----'`--'    `----'`--''--' `---'`--' `--`--'`--`--`--' `----'`--''--'  `--'   `---'  
                                                                                                  ''')
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

                os.system('cls')
                def cadastrar_candidato():

                    n = input("\nPressione ENTER para cadastrar um candidato.")
                    print("\nCandidato cadastrado!\n")

                cadastrar_candidato()

            elif (n == 2):

                os.system('cls')
                def editar_candidato():

                    n = input("\nPressione ENTER para editar um candidato.")
                    print("\nCandidato alterado!\n")

                editar_candidato()

            elif (n == 3):

                os.system('cls')
                def buscar_candidato():
                    
                    n = input("\nPressione ENTER para buscar um candidato.")
                    print("\nBuscando Candidatos!\n")

                buscar_candidato()

            elif (n == 4):

                os.system('cls')
                def listar_candidatos():

                    n = input("\nPressione ENTER para listar os candidatos.")
                    print('''
                        - Bolsomito
                        - Lulalixo
                    ''')

                listar_candidatos()

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
    print('''
                                                    
                                                                  
,--.   ,--.       ,--.                                
 \  `.'  /,---. ,-'  '-. ,--,--. ,---. ,--,--. ,---.  
  \     /| .-. |'-.  .-'' ,-.  || .--'' ,-.  || .-. | 
   \   / ' '-' '  |  |  \ '-'  |\ `--.\ '-'  |' '-' ' 
    `-'   `---'   `--'   `--`--' `---' `--`--' `---'  
                                                    ''')

    n = input("\nPressione ENTER para abrir o mesário.\n")
    mesario()

def mesario():
    os.system('cls')
    print('''
                                                            
,--.   ,--.                             ,--.        
|   `.'   | ,---.  ,---.  ,--,--.,--.--.`--' ,---.  
|  |'.'|  || .-. :(  .-' ' ,-.  ||  .--',--.| .-. | 
|  |   |  |\   --..-'  `)\ '-'  ||  |   |  |' '-' ' 
`--'   `--' `----'`----'  `--`--'`--'   `--' `---'  
                                                    ''')

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