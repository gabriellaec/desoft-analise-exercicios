def calcula_aumento(salario):
    if float(salario) > 1250.00:
        aumento = 0.10*salario
    else:
        aumento = 0.15*salario
    return salario
