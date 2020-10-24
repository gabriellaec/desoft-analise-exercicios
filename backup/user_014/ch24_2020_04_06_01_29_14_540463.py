def calcula_aumento (salario):
    salario = int(input('Qual é o salário do funcionário? ')
    if salario <= 1250:
        aumento = salario * 1.15
    else:
        aumento = salario * 1.1
    return aumento