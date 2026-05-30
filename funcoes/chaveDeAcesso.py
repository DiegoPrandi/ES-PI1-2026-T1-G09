import random

# 1. Gera as partes necessárias dos nomes
def gerar_iniciais(nome_completo):
    """
    Esta função é responsável por gerar iniciais a partir de um nome completo.
    O processo consiste em separar o nome em partes, identificar se há pelo menos dois nomes e então formar as iniciais a 
    partir do primeiro e segundo nome. Caso exista apenas uma palavra, são utilizadas as três primeiras letras do nome.

    Args:
        nome_completo (str): Nome completo do usuário.

    Returns:
        str: Iniciais geradas a partir do nome fornecido em letras maiúsculas.
    """
    partes = nome_completo.split()

    if len(partes) >= 2:
        return partes[0][:2].upper() + partes[1][0].upper()
    else:
        return partes[0][:3].upper()


# 2. Gera os 4 números aleatórios
def gerar_numeros():
    """
    Esta função é responsável por gerar um número aleatório de 4 dígitos.

    Args:
        None

    Returns:
        str: Número aleatório gerado no intervalo de 1000 a 9999.
    """
    return str(random.randint(1000, 9999))


# 3. Função principal (gera a chave completa, juntando as iniciais e os números aleatórios)
def gerar_chave_acesso(nome_completo):
    """
    Esta função é responsável por gerar uma chave de acesso a partir do nome completo do usuário.

    Args:
        nome_completo(str): Nome completo do usuário.

    Returns:
        str: Chave de acesso criada a partir das iniciais e de um número aleatório.
    """
    iniciais = gerar_iniciais(nome_completo)
    numeros = gerar_numeros()

    chave = iniciais + numeros

    return chave