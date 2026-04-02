def criptografia(valor): # Criação da função criptografia com o parâmetro valor

    T = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') #É a lista de caracteres para o índice

    valor=valor.upper() # É setado qualquer valor de letra que está em minúsculo para maiúsculo

    # Abaixo o index funciona como o find do scilab, procurando o local de índice 
    # do caractere x, o for percorre cada caractere do cpf definindo-o como x, 
    # onde o index posteriormente salva dentro de uma outra lista o tal índice de x
    I = [T.index(x) for x in valor] 

    P = [] # Criação da lista vazia que vai ser utilizada na pós divisão em pares

    for i in range(0, len(I),2): # Criação de um for até a quantidade de valores que o texto indicado tem, e vai pulando de dois em dois para a quebra ser de 2 em 2
        par = I[i:i+2] # Divisão da lista I em pares em base do indice, ou seja, começa do i=0(primeiro valor da lista) e i+2, pois é tipo o for, que não contabiliza o valor em si, e sim o anterior
        P.append(par) # Aqui basicamente vai adicionando em lista os pares na lista P
        
    if len(I)%2 != 0: # Se o valor da lista I for impar
        ultPar = I[-1] # É pego o último valor da lista
        P.pop() # É deletado a última lista (que seria ímpar)
        P.append([ultPar, ultPar]) # E é criado a última lista com valores duplicados

    chave = [[5,7],[11,8]] # Criação da chave

    mP = [] # Criação da lista multiplicada
    for par in P: # Pegando cada lista (par) dentro de P
        m1 = chave[0][0]*par[0] + chave[0][1]*par[1] # Multiplicando o primeiro valor da primeira linha da chave com o primeiro valor da dupla + a multiplicação entre o segundo valor da primeira linha da chave com o segundo valor da dupla
        m2 = chave[1][0]*par[0] + chave[1][1]*par[1] # Multiplicando o primeiro valor da segunda linha da chave com o primeiro valor da dupla + a multiplicação entre o segundo valor da segunda linha da chave com o segundo valor da dupla
        mP.append([m1, m2]) # É colocado essa soma em lista dentro de mP
    
    mF = []  # Criação da lista final dos números

    for par in mP: # Criação de um for pra pegar cada par dentro de mP      
        par_res = [] # Criação de uma lista para o resto da divisão
        for valorSolo in par: # Criação de um outro for para cada valor dentro do par
            par_res.append(valorSolo % 36)  # Aqui é pego o resto da divisão por 36 de cada valor 
        mF.append(par_res) # Depois é colocado os pares dentro da lista final dos números   
    
    texto_cifrado = [] # Criada a lista para o texto final

    for par in mF: # Um for para cada par dentro de mF
        for valorSolo in par: # Para cada valor dentro dos pares
            texto_cifrado.append(T[valorSolo]) # É indiciado o valor correspondente da lista de caracteres e é colocado dentro da lista texto_cifrado

    texto_cifrado = ''.join(texto_cifrado) # Aqui é utilizado o join pra pegar cada valor do texto_cifrado que estava em lista e colocado um do lado do outro

    return texto_cifrado # É retornado o texto ja criptografado


