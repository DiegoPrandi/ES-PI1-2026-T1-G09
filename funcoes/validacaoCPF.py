#---------- Função para se obter os 4 primeiros dígitos do CPF ----------

def primeiros_quatro_digitos(cpf):

    try:
        # Converte para string e remove sinal negativo
        num_str = str(abs(int(cpf)))
        
        # Retorna os primeiros 4 caracteres
        return num_str[:4]

    except ValueError:

        raise ValueError("Entrada inválida. Forneça um número inteiro.")

#------------------------------------------------------------------------
def validar_cpf(cpf):
    cpf_limpo = ""
    i = 0
    while i < len(cpf):
        if cpf[i] >= '0' and cpf[i] <= '9':
            cpf_limpo += cpf[i] 
        i += 1
    if len(cpf_limpo) != 11:
        return False
    if (cpf_limpo  == "00000000000" or cpf_limpo == "11111111111" or cpf_limpo == "22222222222" or cpf_limpo == "33333333333" or cpf_limpo == "44444444444" or cpf_limpo == "55555555555" or cpf_limpo == "66666666666" or cpf_limpo == "77777777777" or cpf_limpo == "88888888888" or cpf_limpo == "99999999999"):
        return False
    soma = 0 
    peso = 10
    i = 0

    while i < 9:   
        soma += int(cpf_limpo[i]) * peso
        peso -= 1
        i += 1
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    if digito1 != int(cpf_limpo[9]):
        return False
    soma = 0
    peso = 11
    i = 0
    while i < 10:
        soma += int(cpf_limpo[i]) * peso
        peso -= 1
        i += 1
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if digito2 != int(cpf_limpo[10]):
        return False
    return True