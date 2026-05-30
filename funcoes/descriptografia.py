def descriptografia(valor):
    """
    Esta função é responsável por descriptografar um texto previamente criptografado utilizando uma 
    transformação matricial baseada em uma chave 2x2 e uma tabela de caracteres de A-Z e 0-9.
    O processo consiste em converter o texto cifrado em índices numéricos, aplicar a matriz inversa da chave com operação modular em base 36 e converter os 
    valores resultantes novamente em caracteres para reconstruir o texto original.

    Args:
        valor (str): Texto original que será descriptografado.

    Returns:
        str: Texto descriptografado resultante do processo de descriptografia.
    """

    T = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    # A nova chave de descriptografia, que foi descoberta encontrando a matriz inversa da chave da criptografia, onde foi invertido o 8 pelo 5,
    # e colocado negativo dos outros dois valores. Após isso foi feita a multiplicação da diagonal principal menos e diagonal secundaria, que deu o resultado 
    # -37, depois, fazendo o pmodulo, o resultado da 35, pois -37 + 36 = -1, -1 + 36 = 35. Depois disso foi só multiplicar 35 pelos valores da matriz que foi descoberto
    # os números abaixo.
    chave = [[280,-245],[-385,175]] 

    P = [] # Criação da lista vazia que vai ser utilizada na pós divisão em pares

    # Converte caracteres em índices da tabela
    I = [T.index(x) for x in valor]

    # Percorre a lista I de dois em dois elementos, dividindo-a em pares com base nos índices e armazenando cada par na lista P
    for i in range(0, len(valor),2): 
        par = I[i:i+2] 
        P.append(par) 

    mP = [] # Criação da lista multiplicada

    for par in P: # # Percorre cada par de valores da lista P
        m1 = chave[0][0]*par[0] + chave[0][1]*par[1] 
        m2 = chave[1][0]*par[0] + chave[1][1]*par[1] 
        mP.append([m1, m2]) #Armazena o resultado da multiplicação matricial correspondente ao par atual

    mF = []

    ##Percorre cada par resultante da multiplicação matricial, 
    # aplica o módulo 36 em cada valor para manter o intervalo da tabela de caracteres e armazena o par processado na lista final mF.
    for par in mP: 
        par_res = [] 
        for valorSolo in par: 
            par_res.append(valorSolo % 36)  
        mF.append(par_res) 

    texto_descriptografado = [] # Criada a lista para o texto final

    ### Percorre cada par da lista mF e converte cada índice numérico para o caractere correspondente na tabela T, 
    # adicionando o resultado à lista texto_cifrado
    for par in mF: 
        for valorSolo in par: 
            texto_descriptografado.append(T[valorSolo])

    texto_descriptografado = ''.join(texto_descriptografado) # Aqui é utilizado o join pra pegar cada valor do texto_descriptografado que estava em lista e colocado um do lado do outro

    return texto_descriptografado # É retornado o texto descriptografado