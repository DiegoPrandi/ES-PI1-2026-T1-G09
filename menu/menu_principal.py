import os
import menu.gerenciamento as gerenciamento
from funcoes import ascii
import menu.votacao as votacao


def menu():
    os.system('cls')
    ascii.menuASCII()

    print('''
    1. Gerenciamento
    2. Votação
    3. Sair
    ''')

    n = int(input("-> "))

    if n == 1:
        gerenciamento.gerenciamento()
    elif n == 2:
        votacao.votacao()
    elif n == 3:
        print("Sistema encerrado")