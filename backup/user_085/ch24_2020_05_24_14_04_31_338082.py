def calcula_aumento(salario):
    if salario > 1250.00:
        salario *= 1.1
        return salario
    elif salario <= 1250.00:
        salario *= 1.15
        return salario