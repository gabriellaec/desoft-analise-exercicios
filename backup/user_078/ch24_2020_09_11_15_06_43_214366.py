
def calcula_aumento(salario_perguntado):

    if salario_perguntado > 1250:
        novo_salario = salario_perguntado * 1.10
        return novo_salario

    else:
        novo_salario = salario_perguntado * 1.15
        return novo_salario