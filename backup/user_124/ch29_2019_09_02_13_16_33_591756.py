def calcula_aumento(salario):
    if salario <= 1250:
        aumento = salario + (salario * 0.15)
    elif salario > 1250:
        aumento = salario + (salario * 0.1)
    return aumento