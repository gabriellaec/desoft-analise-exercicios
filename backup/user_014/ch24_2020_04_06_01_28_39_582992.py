def calcula_aumento (salario):
    salario = float(input('Qual é o salário do funcionário? ')
    if salario <= 1250.00:
        aumento = salario * 1.15
    else:
        aumento = salario * 1.1
    return aumento