import os
from database.conexao import conectar

conexao = conectar()
cursor = conexao.cursor()


def login_adm_gerenciamento():

    os.system('cls')

    while True:
        

        usuario_admin = str(input("\nDigite o usuário administrativo: "))
        senha_admin = input("Digite a senha administrativa: ")

        sql = 'SELECT * FROM usuario_adm'
        cursor.execute(sql)
        result = cursor.fetchall()

        for usuario in result:
            if (usuario_admin == usuario[0]) and (senha_admin == usuario[1]):

                os.system('cls')
                print("Logado.")
                return True
        
        print("\nUsuário e senha administrativa incorretos. Tente novamente.")