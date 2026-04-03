import random
from .criptografia import criptografia

# 1. Gera as partes necessárias dos nomes
def gerar_iniciais(nome_completo):
    partes = nome_completo.split()

    if len(partes) >= 2:
        return partes[0][:2].upper() + partes[1][0].upper()
    else:
        return partes[0][:3].upper()


# 2. Gera os 4 números aleatórios
def gerar_numeros():
    return str(random.randint(1000, 9999))


# 3. Função principal (gera a chave completa, juntando as iniciais e os números aleatórios)
def gerar_chave_acesso(nome_completo):
    iniciais = gerar_iniciais(nome_completo)
    numeros = gerar_numeros()

    chave = iniciais + numeros

    chave_criptografada = criptografia(chave) # Criptografa a chave de acesso do eleitor
    
    #Mandar a chave criptografada pro banco

    return chave