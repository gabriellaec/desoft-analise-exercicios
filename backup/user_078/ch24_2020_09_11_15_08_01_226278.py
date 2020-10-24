
def calcula_aumento(salario_perguntado):

    if salario_perguntado > 1250:
        novo_salario = salario_perguntado * 0.10 + salario_perguntado
        return novo_salario

    else:
        novo_salario = salario_perguntado * 0.15 + salario_perguntado
        return novo_salario