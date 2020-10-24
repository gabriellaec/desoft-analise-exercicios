def calcula_aumento(salario):
    if float(salario) > 1250:
        salario = 1.1*salario
        return salario
    else:
        salario = 1.15*salario
        return salario