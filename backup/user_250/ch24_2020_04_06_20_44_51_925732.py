def calcula_aumento(salario):
    if salario > 1250:
        aumento = 1.1*salario
        return aumento
    else:
        aumento = 1.15*salario
        return aumento