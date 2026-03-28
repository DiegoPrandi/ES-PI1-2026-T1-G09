import os
import sistema.candidato as candidato
import sistema.eleitor as eleitor
import sistema.adm as adm
import menu.menu_principal as menu
from funcoes import ascii

def gerenciamento():
    # implementar loop para se digitar um numero diferente de 1 2 3
    # pedir para digitar um numero valido
    os.system('cls')
    
    ascii.gerenciamentoASCII()
    
    print('''
          1. Gestão de Eleitores
          2. Gestão de Candidatos
          3. Voltar
          ''')
    n = int(input('-> '))
    
    if n == 1:
        eleitor.gestao_eleitores()
    elif n == 2:
        if adm.login_adm_gerenciamento():
            candidato.gestao_candidatos()
    elif n == 3:
        menu.menu()