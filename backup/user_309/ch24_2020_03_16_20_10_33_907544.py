def calcula_aumento(salario):
    if salario > 1250:
        aumento = salario * 0.1
    else:
        aumento = salario * 0.15
    return print('seu aumento é de : ',aumento)
