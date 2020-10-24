def calcula_aumento(salario):
    if salario > 1250:
        return salario*(1.1)
    elif salario <= 1250:
        return salario*(1.15)