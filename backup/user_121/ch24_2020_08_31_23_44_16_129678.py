def calcula_aumento(salario):
    if salario > 1250:
        salario *= 1.1
    else:
        salario *= 1.15
    return salario