from menu.menu_principal import menu
from database.conexao import conectar
from funcoes.status_mesario import fecharMesario

conn = conectar()

try:
    menu(conn)

except KeyboardInterrupt:
    print("\nEncerrando sistema...")

finally:
    try:
        fecharMesario()
        conn.close()
    except:
        pass