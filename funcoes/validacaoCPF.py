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
