import os

eleitores

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
        eleitores()
    elif n == 2:
        candidatos()
    elif n == 3:
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
        print('VLW')
        
    else:   
        while True: 
            print('\nDigite alguma opção existente.\n')
            n = int(input('-> '))

menu()