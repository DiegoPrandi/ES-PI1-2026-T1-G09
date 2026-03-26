import mysql.connector
import os
from dotenv import load_dotenv

def conexao():
    load_dotenv()

    conexao = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        port = os.getenv("DB_PORT"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )

    if conexao.is_connected():
        print('Banco conectado')

    cursor = conexao.cursor()
conexao()
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