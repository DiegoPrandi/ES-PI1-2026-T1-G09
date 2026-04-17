import os
import menu.menu_principal as menu
import funcoes.ascii as ascii
import funcoes.status_mesario as statusMesario

def votacao():
    os.system('cls')
    ascii.votacaoASCII()

    n = input("\nPressione ENTER para abrir o mesário.\n")
    mesario()
    
    
def mesario():
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
            def menu_urna():
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
                    if (n == 2):

                        os.system('cls')
                        statusMesario.status_global()
                        input("Pressione ENTER para voltar.")
                        menu_urna()

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
                                    menu_urna()

                                else:
                                    os.system('cls')
                                    statusMesario.abrirMesario()
                                    input("Pressione ENTER para voltar.")
                                    menu_urna()


                            elif (n == 2):

                                if (statusMesario.status_global() == 0):
                                    print("A urna já se encontra fechada.")
                                    input("Pressione ENTER para voltar.")
                                    menu_urna()

                                else:
                                    os.system('cls')
                                    statusMesario.fecharMesario()
                                    input("Pressione ENTER para voltar.")
                                    menu_urna()

                            elif (n == 3):
                                menu_urna()


                            else:
                                print("Opção inválida. Tente novamente.")
                                input("\nPressione ENTER para continuar.")
                                menu_urna()

                        except ValueError:
                            print("Opção inválida. Tente novamente")

                    elif (n == 4):
                        mesario()

                    else:
                        print("\nOpção inválida. Tente novamente.")
                        input("\nPressione ENTER para continuar.")
                        menu_urna()

                except ValueError:
                    print("\nOpção inválida. Tente novamente.")
                    menu_urna()


            menu_urna()
        
        elif (n == 2):
            def resultados_votacao():
                os.system('cls')

                print('''
                    Resultados

                    1. Boletim de Urna
                    2. Estatísticas
                    3. Votos por Partido
                
                ''')

                n = int(input("-> "))

            resultados_votacao()

        elif (n == 3):
            def auditoria_votacao():
                os.system('cls')

                print('''
                    Auditoria

                    1. Ver Logs
                    2. Ver Protocolos
                
                ''')

                n = int(input("-> "))

            auditoria_votacao()
        
        elif (n == 4):
            os.system('cls')
            menu.menu()
            
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar.")
            mesario()  
            
    except ValueError:
        print("Opção inválida. Tente novamente.")
        input("\nPressione ENTER para continuar.")
        mesario()
    