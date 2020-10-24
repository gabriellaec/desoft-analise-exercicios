def calcula_aumento(salario):
    if salario>1250.00:
        a = 1.1*salario
        return a
    elif salario<=1250.00:
        b = 1.15*salario
        return b