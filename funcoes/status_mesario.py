import time
from funcoes.zerezima import zerezima
from funcoes.log_ocorrencia import registrar_log
status_mesario = 0

def abrirMesario(conn):
    """
    Esta função é responsável por abrir a urna, modificando o valor da variável status_mesario para 1 e exibir a mensagem de "abrindo urna".

    Args:
        conn (mysql.connector): Conexão ativa com o banco de dados MySQL.

    Returns:
        None: A função não retorna valores, apenas muda o valor do status_mesario para 1.
    """
    global status_mesario
    status_mesario = 1
    zerezima(conn)
    
    print('Abrindo urna, aguarde...')
    time.sleep(1.7)
    print("A urna foi aberta.")
    registrar_log("ABERTURA", "Votação iniciada com sucesso. Total de votos zerados.") # Registra no log a abertura da urna

def fecharMesario():
    """
    Esta função é responsável por fechar a urna, modificando o valor da variável status_mesario para 0 e exibir a mensagem de "fechando urna".

    Args:
        None.

    Returns:
        None: A função não retorna valores, apenas muda o valor do status_mesario para 0.
    """
    global status_mesario
    status_mesario = 0

    print('Fechando urna, aguarde...')
    time.sleep(1.7)
    print("A urna foi fechada.")
    registrar_log("ENCERRAMENTO", "Votação finalizada com sucesso.") # Registra no log o encerramento da urna


def status_global():
    """
    Esta função é responsável por mostrar se a urna está aberta ou fechada, retornando os valores da variável status_mesario.

    Args:
        None.

    Returns:
        int: A função retorna o valor do status_mesario, para a identificação da urna aberta ou fechada.
    """
    if status_mesario == 0:
        return 0

    elif status_mesario == 1:
        return 1