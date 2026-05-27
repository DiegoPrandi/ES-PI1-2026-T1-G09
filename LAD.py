from menu.menu_principal import menu
from database.conexao import conectar
from funcoes.status_mesario import fecharMesario
import time
import os

conn = conectar()

try:
    os.system('cls')
    print('Iniciando sistema, aguarde...')
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    menu(conn)

except KeyboardInterrupt:
    print("\nEncerrando sistema...")

finally:
    try:
        fecharMesario()
        conn.close()
    except:
        pass