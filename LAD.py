from menu.menu_principal import menu
from database.conexao import conectar

conn = conectar()

try:
    menu(conn)

except KeyboardInterrupt:
    print("\nEncerrando sistema...")

finally:
    try:
        conn.close()
    except:
        pass