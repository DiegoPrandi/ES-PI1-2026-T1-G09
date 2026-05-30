from datetime import datetime
import os

# -- Cria uma pasta chamada "logs", ao qual irá armazenar todos os arquivos de log de ocorrência, caso ela já exista, o código não criará uma nova pasta.

os.makedirs("logs", exist_ok=True)

# -- Define o nome do arquivo de log de ocorrência, utilizando a data e hora atual para garantir que cada arquivo seja único.

arquivo_log = datetime.now().strftime(
    "logs/log_ocorrencias_%Y-%m-%d_%H-%M-%S.txt"
)

# -- Registra um evento no arquivo de log de ocorrência.
#
#       A função necessita que sejam passado dois parâmetros nela:
#           - Tipo do evento (string): Registra o tipo do evento (ABERTURA, ENCERRAMENTO, ALERTA, SUCESSO ... etc)
#           - Mensagem (string): Registra a descrição do log de evento ocorrido

def registrar_log(tipo_evento, mensagem):
    """
    Esta função é responsável por registrar logs de ocorrência em um arquivo texto (.txt).

    Args:
        tipo_evento (str): O tipo de evento do log.
        mensagem (str): A mensagem que deverá ser escrita no arquivo de texto (.txt).

    Returns:
        None: A função não retorna valores, apenas registra informações no arquivo de log.
    """

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linha_terminal = f"[{data_hora}] {tipo_evento}: {mensagem}\n"

    with open(arquivo_log, "a", encoding="utf-8") as arq:
        arq.write(linha_terminal)

# -- Exibe todos os logs que ocorreram durante o processo de eleição.
#       
#       O loop tenta ler o arquivo "arquivo_log", se houver algum log sequer, a função printa ela, se não houver, printa erro.

def exibir_logs():
    """
    Esta função é responsável por exibir o arquivo de texto (.txt) dos logs.

    Args:
        None.

    Returns:
        None: A função não retorna valores, apenas printa as informações do arquivo de texto.
    """
    try:
        with open(arquivo_log, "r", encoding="utf-8") as arq:
            print("\n========== LOG DE OCORRÊNCIAS ==========\n")
            print(arq.read())
    
    except FileNotFoundError:
        print("Nenhum log encontrado. Tente novamente.")