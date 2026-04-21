import os
import menu.menu_principal as menu
import funcoes.ascii as ascii
import funcoes.status_mesario as statusMesario
from sistema.voto import login
from sistema.voto import verificar_voto
from sistema.voto import adicionar_voto

def votacao(conn):
    os.system('cls')
    ascii.votacaoASCII()

    n = input("\nPressione ENTER para abrir a votação.\n")
    mesario(conn)

def mesario(conn):
    os.system('cls')
    ascii.mesarioASCII()

    print('''
        Digite o valor da opção desejada:

        1. Menu da Urna
        2. Resultados
        3. Auditoria
        4. Voltar
    ''')
    try:
        n = int(input("-> "))
    
        
        if (n == 1):
            def menu_urna(conn):
                os.system('cls')

                print('''
                        Menu da Urna

                        1. Votar
                        2. Status da Urna
                        3. Gerenciar Urna
                        4. Voltar
                
                    ''')

                n = int(input("-> "))
                try:
                    if (n == 1):
                        id_eleitor = login(conn) # Guardando o valor de retorno da função login
                        status_voto = verificar_voto(id_eleitor, conn) #Guardando o valor de retorno da função verificar_voto e utilizando o parâmetro da variável acima
                        if status_voto == 1: # Verifica se o status de voto do eleitor é igual a 1
                            print("Você ja votou!")
                            input("Pressione ENTER para voltar.")
                            menu_urna(conn)
                        else:
                            adicionar_voto(id_eleitor, conn) # Puxa a função adicionar_voto com o parâmetro do id do eleitor

                        input("Pressione ENTER para voltar.")
                        menu_urna(conn)

                    elif (n == 2):

                        os.system('cls')
                        statusMesario.status_global()
                        input("Pressione ENTER para voltar.")
                        menu_urna(conn)

                    elif (n == 3):
                        os.system('cls')                        

                        print('''

                            Escolha uma das seguintes opções
                              
                            1. Abrir urna
                            2. Fechar urna
                            3. Voltar

                        ''')

                        n = int(input("-> "))

                        try:
                            
                            if (n == 1):

                                if (statusMesario.status_global() == 1):
                                    print("A urna já se encontra aberta.")
                                    input("Pressione ENTER para voltar.")
                                    menu_urna(conn)

                                else:
                                    os.system('cls')
                                    statusMesario.abrirMesario()
                                    input("Pressione ENTER para voltar.")
                                    menu_urna(conn)


                            elif (n == 2):

                                if (statusMesario.status_global() == 0):
                                    print("A urna já se encontra fechada.")
                                    input("Pressione ENTER para voltar.")
                                    menu_urna(conn)

                                else:
                                    os.system('cls')
                                    statusMesario.fecharMesario()
                                    input("Pressione ENTER para voltar.")
                                    menu_urna(conn)

                            elif (n == 3):
                                menu_urna(conn)


                            else:
                                print("Opção inválida. Tente novamente.")
                                input("\nPressione ENTER para continuar.")
                                menu_urna(conn)

                        except ValueError:
                            print("Opção inválida. Tente novamente")

                    elif (n == 4):
                        mesario(conn)

                    else:
                        print("\nOpção inválida. Tente novamente.")
                        input("\nPressione ENTER para continuar.")
                        menu_urna(conn)

                except ValueError:
                    print("\nOpção inválida. Tente novamente.")
                    menu_urna(conn)


            menu_urna(conn)
        
        elif (n == 2):
            def resultados_votacao(conn):
                os.system('cls')
                n = 0
                while n!= 1 and n!= 2 and n!= 3:
                    print('''
                    Resultados

                    1. Boletim de Urna
                    2. Estatísticas
                    3. Votos por Partido
                    ''')
                    n = int(input("-> "))
                    if n!= 1 and n!= 2 and n!= 3:
                        print("Opção inválida. Tente novamente.")
            resultados_votacao(conn)

        elif (n == 3):
            def auditoria_votacao(conn):
                os.system('cls')
                n = 0
                while n!= 1 and n!= 2:
                    print('''
                    Auditoria

                    1. Ver Logs
                    2. Ver Protocolos
                    ''')
                    n = int(input("-> "))
                    if n!= 1 and n!= 2:
                     print("Opção inválida. Tente novamente.")

            auditoria_votacao(conn)
        
        elif (n == 4):
            os.system('cls')
            menu.menu(conn)
            
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar.")
            mesario(conn)  
            
    except ValueError:
        print("Opção inválida. Tente novamente.")
        input("\nPressione ENTER para continuar.")
        mesario(conn)
