import os
from database.conexao import conectar
import menu.menu_principal as menu
import menu.gerenciamento as gerenciamento

conexao = conectar()
cursor = conexao.cursor()

def gestao_candidatos():

            os.system('cls')
            print('''
            \nDigite o número da opção desejada.

            1. Cadastrar Candidato
            2. Editar Candidato
            3. Buscar Candidato
            4. Listar Candidatos
            5. Voltar
            ''')
            try:
                n = int(input("-> "))
            

                if (n == 1):
                    # implementar a verificação para não adicionar
                    # um candidato com o mesmo número e partido...
                    def cadastrar_candidato():
                        os.system('cls')
                        name = str(input('Digite o nome do candidato: '))
                        number = int(input('Digite o número do candidato: '))
                        partido = str(input('Digite o partido do candidato: '))
                        
                        sql = 'INSERT INTO candidatos (nome_completo, numero_votacao, nome_partido) VALUES (%s, %s, %s)'
                        val = (name, number, partido)

                        cursor.execute(sql, val)
                        conexao.commit()
                        
                        print("\nCandidato cadastrado!\n")
                        input('Pressione ENTER para voltar.')
                        
                        gestao_candidatos()
                    cadastrar_candidato()


                elif (n == 2):
                    os.system('cls')
                    def editar_candidato():

                        nome = str(input("Digite o nome do candidato que deseja alterar: "))
                        sql = 'SELECT * FROM candidatos'
                        cursor.execute(sql)
                        result = cursor.fetchall()

                        '''
                                na nossa tabela candidatos tem os campos
                                id    nome   numero   partido
                                0      1       2        3
                                entao os indice no for fica assim
                                id e o indice 0, nome e o indice 1, numero e o indice 2 e partido e o indice 3
                                por isso do candidato[1]
                                pq ele percorre todos os candidatos
                                se algum cadidato tiver o nome igual ele vai pro if

                                resumindo, o for faz o seguinte
                                
                                para cada candidato na tabela candidatos (ele pega todos os candidatos)
                                se o nome digitado for igual ao nome do candidato (candidato[1])
                                fecho acho o homi  
                        '''
                        encontrado = False
                        for candidato in result:
                            if nome == candidato[1]:
                                encontrado = True
                                print(f"\nCandidato encontrado: {candidato[1]} | Número: {candidato[2]} | Partido: {candidato[3]}\n")
                                name = str(input("Digite um novo nome para o candidato: "))
                                number = int(input("Digite o número do partido: "))
                                partido = str(input("Digite o nome do partido: "))

                                sql = 'UPDATE candidatos SET nome_completo=%s, numero_votacao=%s, nome_partido=%s WHERE id=%s'
                                values = (name, number, partido, candidato[0])

                                cursor.execute(sql, values)
                                conexao.commit()

                                print("\nCandidato alterado!")
                                input("\nPressione ENTER para voltar.")
                                gestao_candidatos()
                                break
                        
                        if not encontrado:
                            print("\nCandidato não encontrado.\n")
                            input("Pressione ENTER para voltar.")
                            gestao_candidatos()
                                
                    editar_candidato()

                elif (n == 3):

                    os.system('cls')
                    def buscar_candidato():
                        nome = str(input("\nDigite o nome do candidato: "))
                        sql = 'SELECT * FROM candidatos'
                        cursor.execute(sql)
                        result = cursor.fetchall()
                        
                        print("\nCandidatos encontrados:\n")
                        print('-' * 120)
                        for candidato in result:
                            if nome == candidato[1]:
                                print(f"Nome: {candidato[1]} | Número: {candidato[2]} | Partido: {candidato[3]}")
                        print('-' * 120)
                        input('\nPressione ENTER para voltar.')
                        gestao_candidatos()
                    buscar_candidato()

                elif (n == 4):
                    # melhorar a exibicao dos candidatos
                    # deixar mais bonito 
                    os.system('cls')
                    def listar_candidatos():
                        sql = 'SELECT * FROM candidatos'
                        cursor.execute(sql)
                        result = cursor.fetchall()

                        print("\nCandidatos cadastrados:\n")
                        print('-' * 120)
                        for candidato in result:
                            print(f"Nome: {candidato[1]} | Número: {candidato[2]} | Partido: {candidato[3]}")
                        print('-' * 120)

                    listar_candidatos()
                    input('\nPressione ENTER para voltar.')
                    gestao_candidatos()

                elif (n == 5):

                    os.system('cls')
                    gerenciamento.gerenciamento()
                
                else:
                    print("Opção inválida. Tente novamente.")
                    input("\nPressione ENTER para continuar.")
                    gestao_candidatos()
            except ValueError:
                print("Opção inválida. Tente novamente.")
                input("\nPressione ENTER para continuar.")
                gestao_candidatos()

            