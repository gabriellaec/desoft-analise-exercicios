def calcula_aumento(salario):
    if salario > 1250:
        y = salario * 1.1
    elif salario <= 1250:
        y = salario * 1.15
    return y