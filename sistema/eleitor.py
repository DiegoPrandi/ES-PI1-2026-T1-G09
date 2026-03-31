import os
import menu.gerenciamento as gerenciamento
import funcoes.chaveDeAcesso as chaveDeAcesso
import funcoes.criptografia as criptografia
import funcoes.validacaoCPF as validacaoCPF
from funcoes import ascii as ascii
import sistema.adm as adm

'''
    por enquanto nenhuma funcao esta implementada
    aqui tem que fazer tudo, e tem a parte  da criptograffia
    e a parte de validao do cpf criacao da chave de acesso
    tem umas coisinha aqui
    
    eu fiz 3 arquivos na pasta funcoes
    chaveDeAcesso.py
    criptografia.py
    validacaoCPF.py
    
    ai usa esses arquivos para fazer a logica
    e fazer funfar    
    essas funcoes fazem na hora de cadastrar um eleitor
    criptografar a chave de acesso, validar o cpf e criar a chave de acesso
    
    na parte de editar, tem que solicitar o cpf do eleitor
    a senha dele,  tudo dele, pq se nao ele pode editar o usuario de outra pessoa
    
    ai buscar e listar, acredito que seja ja opcao de adm, pq nao faz sentido
    um eleitor buscar outro ou listar tlgd? entao faz essa validao antes
    igual no candidato que tem essa validacao de adm    
'''
def gestao_eleitores():
            os.system('cls')
            
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
                    adm.login_adm_gerenciamento()


                editar_remover_eleitor()

            elif (n == 3):

                os.system('cls')

                def buscar_eleitores():
                    adm.login_adm_gerenciamento()

                    n = input("\nPressione ENTER para buscar eleitores.")
                    print("\nBuscando eleitores!\n")

                buscar_eleitores()

            elif (n == 4):

                os.system('cls')

                def listar_eleitores():
                    adm.login_adm_gerenciamento()

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