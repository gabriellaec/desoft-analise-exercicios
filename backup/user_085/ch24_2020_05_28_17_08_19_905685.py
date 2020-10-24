def calcula_aumento(salario):
    if salario > 1250.00:
        salario *= 1.1
        return '{:.2f}'.format(salario, '.f')
    elif salario <= 1250.00:
        salario *= 1.15
        return '{:.2f}'.format(salario)