def calcula_irrf():
    
    salario = input('Valor do salario')
    dependentes = int(input('Numero de dependentes'))

    if salario <= 1045:
        inss = salario*0.075
    if 1045 < salario <= 2089.6:
        inss = salario*0.09
    if 2089.6 < salario <= 3134.4:
        inss = salario*0.12
    if 3134.4 < salario <= 6101.06:
        inss = salario*0.14
    else:
        inss = 671.12
    
    x = salario - inss - dependentes*189.59
    
    if x <= 1903.98:
        aliq = 0
        ded = 0
    if 1903.98 < x <= 2826.65:
        aliq = 0.075
        ded = 142.8
    if 2826.65 < x <= 3751.05:
        aliq = 0.15
        ded = 354.8
    if 3571.05 < x <= 4664.68:
        aliq = 0.225
        ded = 636.13
    else:
        aliq = 0.275
        ded = 869.36
    
    IRRF = (x*aliq) - ded
    
    print('o IRRF é de R${0}".format(IRRF)