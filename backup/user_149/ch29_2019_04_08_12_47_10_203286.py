def calcula_aumento(salario):
    aumento = 0
    if salario>1250.00:
        aumento = 0.1*salario
    elif salario<=1250.00:
        aumento = 0.15*salario
    return aumento + salario 