def calcula_aumento(salario):
    if salario>1250.00:
        a = 0.1*salario
        return a
    if salario<=1250.00:
        b = 0.15*salario
        return b