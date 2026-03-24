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
        gestao_eleitores()
    elif n == 2:
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