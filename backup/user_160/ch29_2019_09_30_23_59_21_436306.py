def calcula_aumento(salario):
    aumento = 0
    if salario > 1250:
        aumento = salario *0.1
    else:
        aumento = salario *0.15
    return aumento