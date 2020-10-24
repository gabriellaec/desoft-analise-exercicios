
def calcula_aumento(salario_perguntado):

    if salario_perguntado > 1250:
        salario_perguntado *= 1.10
        return salario_perguntado

    else:
        salario_perguntado *= 1.15
        return salario_perguntado
