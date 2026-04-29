# Função para carregar o status do mesário em um arquivo

def carregar_status():
    try:
        with open("status_mesario.txt", "r") as arq:
            return int(arq.read())

    except FileNotFoundError:
        return 0  # Se não houver, começa fechado

# Função para salvar o status no arquivo

def salvar_status(status):
    with open("status_mesario.txt", "w") as arq:
        arq.write(str(status))

status_mesario = carregar_status() #Seta uma variável global como o status que foi carregado

def abrirMesario():
    global status_mesario
    status_mesario = 1
    salvar_status(status_mesario)

    print("A urna foi aberta.")

def fecharMesario():
    global status_mesario
    status_mesario = 0
    salvar_status(status_mesario)

    print("A urna foi fechada.")

def status_global():

    if status_mesario == 0:
        print("\nA urna está fechada.")
        return 0

    elif status_mesario == 1:
        print("\nA urna está aberta.")
        return 1