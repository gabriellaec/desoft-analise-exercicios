def calcula_aumento(salario):
    if salario > 1250:
        y = salario*1.1-salario
        return y
    if salario <= 1250:
        y = salario*1.15-salario
        return y