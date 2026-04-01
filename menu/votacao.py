import os
import menu.menu_principal as menu
import funcoes.ascii as ascii

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
    n = int(input("-> "))
    try:
        
        if (n == 1):
            def menu_urna():
                os.system('cls')

                print('''
                        Menu da Urna

                        1. Votar
                        2. Encerrar
                
                    ''')

                n = int(input("-> "))
                try:
                    if (n == 1):
                        print("Você votou!")

                    elif (n == 2):
                        print("Sistema encerrado.")
                    else:
                        print("Opção inválida. Tente novamente.")
                        input("\nPressione ENTER para continuar.")
                        menu_urna()
                except ValueError:
                    print("Opção inválida. Tente novamente.")
                    input("\nPressione ENTER para continuar.")
                    menu_urna()


                # else:

                #     while True:
                #         print("\nDigite uma opção válida.\n")
                #         n = int(input("-> "))

                #         if (n == 1):
                #             print("Você votou!")
                #             break

                #         elif (n == 2):
                #             print("\nSistema encerrado.\n")
                #             break
                    

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
    