import os
import mysql.connector

def gerenciamento():
    os.system('cls')
    print('''                                                                                                  
 ,----.                                      ,--.                                   ,--.          
'  .-./    ,---. ,--.--. ,---. ,--,--,  ,---.`--' ,--,--.,--,--,--. ,---. ,--,--, ,-'  '-. ,---.  
|  | .---.| .-. :|  .--'| .-. :|      \| .--',--.' ,-.  ||        || .-. :|      \'-.  .-'| .-. | 
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
        4. Sair
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
        print('VLW')
        
    else:   
        while True: 
            print('\nDigite alguma opção existente.\n')
            n = int(input('-> '))

menu()