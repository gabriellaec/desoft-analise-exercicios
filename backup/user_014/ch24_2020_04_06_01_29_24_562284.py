def calcula_aumento (salario):
    salario = int(input('Qual é o salário do funcionário? ')
    if salario <= 1250:
        aumento = salario * 0.15
    else:
        aumento = salario * 0.1
    return aumento