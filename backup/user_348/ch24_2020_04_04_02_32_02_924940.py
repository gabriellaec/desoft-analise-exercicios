def calcula_aumento (salário):
    salário = float(input('Qual é o salário: ')
    if salário > 1250.00:
        salário = 1.1*salário
    else:
        salário = 1.15*salário
    return salário