import os
import menu.gerenciamento as gerenciamento
import funcoes.chaveDeAcesso as chaveDeAcesso
from funcoes.chaveDeAcesso import gerar_chave_acesso
import funcoes.criptografia as criptografia
import funcoes.validacaoCPF as validacaoCPF
from funcoes import ascii as ascii
import sistema.adm as adm
from funcoes.validacaoCPF import primeiros_quatro_digitos
from database.conexao import conectar
import mysql.connector
from funcoes.criptografia import criptografia
from funcoes.validacaoCPF import validar_cpf
from funcoes.validacao_TituloEleitor import validar_titulo_eleitor

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
            try:
                n = int(input("-> "))
             
                if (n == 1):

                    os.system('cls')

                    def cadastrar_eleitor():
                        nome_completo = str(input("Digite seu nome completo: "))
                        
                        cpf = str(input("Digite seu CPF: "))
                        while validar_cpf(cpf) ==False:
                            print("CPF inválido. Tente novamente: ")
                            cpf = str(input("Digite seu CPF: "))
                        print("CPF válido!")
                        
                        titulo_eleitor = str(input("Digite seu título de eleitor: "))
                        while validar_titulo_eleitor(titulo_eleitor) == False:
                            print("Título de eleitor inválido. Tente novamente:")
                            titulo_eleitor = str(input("Digite seu título de eleitor: "))
                        print("Título válido!")

                        print('''
                            Você atuará como mesário?
                            1. Sim
                            2. Não
                        ''')
                        n = int(input("-> "))

                        if n == 1:
                            mesario = 1
                            
                            n = input("Pressione ENTER para voltar.")
                            gestao_eleitores()

                        elif n == 2:
                            mesario = 0

                            n = input("Pressione ENTER para voltar.")
                            gestao_eleitores()
                            
                        else:
                            print("Opção inválida. Tente novamente.")
                            return

                        status_voto = 0 # Variável de votação

                        chave_normal = gerar_chave_acesso(nome_completo)
                        print(f"Chave de acesso gerada: {chave_normal}")

                        cpf_criptografado = criptografia(cpf) # Criptografa o cpf
                        chave_acesso = criptografia(chave_normal) # Criptografa a chave de acesso

                        conn = conectar() # Criação da conexão com o banco
                        
                        try: 
                            cursor = conn.cursor() # Criando um "cursor" dentro do banco, para fazermos as modificações
                            
                            cursor.execute('''
                                INSERT INTO eleitores (chave_acesso, nome_completo, titulo_eleitor, cpf_criptografado, mesario, status_voto)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            ''', (chave_acesso, nome_completo, titulo_eleitor, cpf_criptografado, mesario, status_voto)) # Colocando os dados no banco

                            conn.commit() # Commitando os dados no banco

                        except  mysql.connector.IntegrityError: # Tratando erros de duplicidade
                            print("\nErro: CPF já cadastrado no sistema!")
                        
                        finally: # Quando tudo acima tiver feito fecha o cursor e a conexão com o banco
                            cursor.close()
                            conn.close()

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

                        nome = str(input("\nDigite o nome do eleitor: ")).strip()
                        sql = "SELECT * FROM eleitores WHERE LOWER(nome_completo) LIKE ?"
                        cursor.execute(sql, (f"%{nome.lower()}%",))
                        result = cursor.fetchall()
                        
                        print("\nEleitores encontrados:\n")
                        print('-' * 120)
                        for eleitor in result:
                            print(f"Nome: {eleitor[2]}")
                        print('-' * 120)
                        input('\nPressione ENTER para voltar.')

                    buscar_eleitores()

                elif (n == 4):

                    os.system('cls')

                    def listar_eleitores():
                        adm.login_adm_gerenciamento()

                        n = input("\nPressione ENTER para listar todos os eleitores.")
                        sql = "SELECT * FROM eleitores"
                        cursor.execute(sql)
                        result = cursor.fetchall()

                        print("Lista de eleitores:")
                        print('-' * 120)
                        for eleitor in result:
                            print(f"Nome Completo: {eleitor[2]} | Chave de Acesso: {eleitor[1]} | Título de Eleitor: {eleitor[3]} | CPF Criptografado: {eleitor[4]} | Mesário: {eleitor[5]} | Status do Voto: {eleitor[6]}")
                        print('-' * 120)

                    listar_eleitores()

                elif (n == 5):
                    os.system('cls')
                    gerenciamento.gerenciamento()
                else:
                    print("Opção inválida. Tente novamente.")
                    input("\nPressione ENTER para continuar.")
                    gestao_eleitores()
                    
            except ValueError:
                print("Opção inválida. Tente novamente.")
                input("\nPressione ENTER para continuar.")
                gestao_eleitores()
