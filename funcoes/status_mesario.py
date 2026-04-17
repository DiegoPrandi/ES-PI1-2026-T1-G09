#status_mesario = 0 #Seta uma variável global de padronização

def abrirMesario():
    global status_mesario
    status_mesario = 1

    print("A urna foi aberta.")

def fecharMesario():
    global status_mesario
    status_mesario = 0

    print("A urna foi fechada.")

def status_global():

    if status_mesario == 0:
        print("A urna está fechada.")

    elif status_mesario == 1:
        print("A urna está aberta.")