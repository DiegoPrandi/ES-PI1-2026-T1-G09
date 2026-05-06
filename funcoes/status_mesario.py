from funcoes.zerezima import zerezima
status_mesario = 0

def abrirMesario(conn):
    global status_mesario
    status_mesario = 1
    zerezima(conn)

    print("A urna foi aberta.")

def fecharMesario():
    global status_mesario
    status_mesario = 0

    print("A urna foi fechada.")

def status_global():

    if status_mesario == 0:
        return 0

    elif status_mesario == 1:
        return 1