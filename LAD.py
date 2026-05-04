from menu.menu_principal import menu
from database.conexao import conectar
from funcoes.status_mesario import fecharMesario
import funcoes.zerezima as zerezima

conn = conectar()

try:
    zerezima.zerezima(conn)
    menu(conn)

except KeyboardInterrupt:
    print("\nEncerrando sistema...")

finally:
    try:
        fecharMesario()
        conn.close()
    except:
        pass