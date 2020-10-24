def calcula_aumento(salario):
    if float(salario) > 1250:
        salario = 0.1*salario
        return salario
    else:
        salario = 0.15*salario
        return salario