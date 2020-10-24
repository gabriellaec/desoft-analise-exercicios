def IRRF():
    salario = int(input('Qual o seu salário? '))
    dependentes = int(input('Quantos dependentes possui? '))

    contribuicao = 0
    if salario <= 1045:
        contribuicao = salario * 0.075

    elif 1045 < salario <= 2089.60:
        contribuicao = salario * 0.09

    elif 2089.60 < salario <= 3134.40:
        contribuicao = salario * 0.12

    elif 3134.40 < salario <= 6101.06:
        contribuicao = salario * 0.14

    else:
        contribuicao = 671.12

    base_calculo = salario - contribuicao - dependentes * 189.59

    valor_IRRF = 0
    if base_calculo <= 1903.98:
        valor_IRRF = 0
    
    elif 1903.98 < base_calculo <= 2826.65:
        valor_IRRF = base_calculo * 0.075 - 142.80
    
    elif 2826.65 < base_calculo <= 3751.05:
        valor_IRRF = base_calculo * 0.15 - 354.80

    elif 3751.05 < base_calculo <= 4664.68:
        valor_IRRF = base_calculo * 0.225 - 636.13
    
    else:
        valor_IRRF = base_calculo * 0.275 - 869.36

    return valor_IRRF