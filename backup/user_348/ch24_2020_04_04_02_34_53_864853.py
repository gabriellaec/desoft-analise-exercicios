def calcula_aumento (salário):
    salário = int(input('Qual é o salário: '))
    if salário > 1250.00:
        a = 0.1*salário
    else:
        a = 0.15*salário
    return a