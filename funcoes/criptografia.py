def criptografia(valor): # Criação da função criptografia com o parâmetro valor
    """
    Esta função é responsável por criptografar um texto utilizando uma transformação matricial baseada em uma chave 2x2 e uma tabela de caracteres de A-Z e 0-9.
    O processo consiste em converter o texto para letras maiúsculas, transformá-lo em índices numéricos com base na tabela de caracteres, agrupá-los em pares e aplicar 
    uma multiplicação matricial com uma chave pré-definida. Em seguida, é aplicado o módulo 36 para manter os valores dentro do intervalo da tabela e 
    os resultados são convertidos novamente em caracteres para gerar o texto criptografado.

    Args:
        valor (str): Texto original que será criptografado.

    Returns:
        str: Texto criptografado resultante do processo de codificação.

    """

    T = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') #É a lista de caracteres para o índice

    valor=valor.upper() # É setado qualquer valor de letra que está em minúsculo para maiúsculo

    # Converte caracteres em índices da tabela
    I = [T.index(x) for x in valor] 

    P = [] # Criação da lista vazia que vai ser utilizada na pós divisão em pares

    # Percorre a lista I de dois em dois elementos, dividindo-a em pares com base nos índices e armazenando cada par na lista P
    for i in range(0, len(I),2): 
        par = I[i:i+2] 
        P.append(par) 
        
    ## Verifica se a quantidade de elementos em I é ímpar; 
    # caso seja, remove o último par incompleto e cria um novo par duplicando o último elemento para manter a consistência da divisão em pares.
    if len(I)%2 != 0: 
        ultPar = I[-1] 
        P.pop() 
        P.append([ultPar, ultPar]) 

    chave = [[5,7],[11,8]] # Criação da chave

    mP = [] # Criação da lista multiplicada
    for par in P:  # Percorre cada par de valores da lista P
        m1 = chave[0][0]*par[0] + chave[0][1]*par[1] 
        m2 = chave[1][0]*par[0] + chave[1][1]*par[1] 
        mP.append([m1, m2]) # Armazena o resultado da multiplicação matricial correspondente ao par atual
    
    mF = []  # Criação da lista final dos números

    #Percorre cada par resultante da multiplicação matricial, 
    # aplica o módulo 36 em cada valor para manter o intervalo da tabela de caracteres e armazena o par processado na lista final mF.
    for par in mP:      
        par_res = [] 
        for valorSolo in par: 
            par_res.append(valorSolo % 36)  
        mF.append(par_res)   
    
    texto_cifrado = [] # Criada a lista para o texto final

    ## Percorre cada par da lista mF e converte cada índice numérico para o caractere correspondente na tabela T, 
    # adicionando o resultado à lista texto_cifrado
    for par in mF: 
        for valorSolo in par: 
            texto_cifrado.append(T[valorSolo]) 

    texto_cifrado = ''.join(texto_cifrado) # Aqui é utilizado o join pra pegar cada valor do texto_cifrado que estava em lista e colocado um do lado do outro

    return texto_cifrado # É retornado o texto ja criptografado