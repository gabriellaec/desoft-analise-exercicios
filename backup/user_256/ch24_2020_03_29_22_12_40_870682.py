def calcula_aumento(salario):
    if salario>1250.00:
        a = 1.1*salario
        return a
    if salario<=1250.00:
        b = 1.15*salario
        return b