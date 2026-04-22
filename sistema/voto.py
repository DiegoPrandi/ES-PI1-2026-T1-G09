'''
    menu -> votacao - > voto.py
    aqui tem que implementar a parte de votar
    pedir pro eleitor realizar o login 
    validar no banco a senha, ver se ja votou, cpf e valido...
'''

import os
from database.conexao import conectar
import mysql.connector
from funcoes.criptografia import criptografia
from funcoes.validacaoCPF import validar_cpf

conexao = conectar()
cursor = conexao.cursor()

# Função para cadastro de voto
    # - Pede o nome completo, a chave de acesso e o título de eleitor.
    # - Faz uma leitura do banco na tabela de eleitores e retorna o resultado.
    # - É criado um laço pra conseguir agrupar as colunas com os respectivos valores dos inputs.
    # - Verifica se o eleitor possue voto ou não, e se as credenciais batem com as que existem no banco de dados.
    # - Autoriza o cadastro do eleitor.

def cadastroVoto():

    nome = input("Digite seu nome completo: ").strip().lower()
    chave_acesso = input("Digite sua chave de acesso: ").strip()
    titulo_eleitor = input("Digite seu título de eleitor: ").strip()

    sql = ''' 
        SELECT * FROM eleitores
        WHERE nome_completo = %s
        AND chave_acesso = %s
        AND titulo_eleitor = %s
        '''

    val = (nome, criptografia(chave_acesso), titulo_eleitor)
    cursor.execute(sql, val)
    result_eleitor = cursor.fetchone()

    if result_eleitor:
        if result_eleitor[6] == False:
            print("\nVoto cadastrado!")
            input("Pressione ENTER para continuar.")
            os.system('cls')
        else:
            print("O eleitor indicado já votou.")
    else:
        print("\nNome, chave de acesso ou título de eleitor inválido.\n")
        cadastroVoto()

