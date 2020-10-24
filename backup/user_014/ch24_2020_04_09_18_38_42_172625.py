def calcula_aumento(salario):
    salario = float(input('Qual é o salário? '))
    if salario > 1250.00:
        aumento = 0.1 * salario
    else:
        aumento = 0.15 * salario
    return aumento