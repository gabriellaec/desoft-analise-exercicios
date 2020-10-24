salario = float(input('Qual o seu salário bruto? '))
dependentes = int(input('Qual o número de dependentes? '))
if salario <= 1045:
    contribuicao = salario*0.075
elif 1045.01 <= salario <= 2089.60:
    contribuicao = salario*0.09
elif 2089.61 <= salario <= 3134.40:
    contribuicao = salario*0.012
elif 3134.41 <= salario <= 6101.06:
    contribuicao = salario*0.14
elif salario > 6101.06: 
    contribuicao = 671.12
def base_de_calculo(salario, dependentes, contribuicao):
    y = salario - contribuicao - dependentes*189.59
    return y
def irrf(base_de_calculo):
    if base_de_calculo(salario, dependentes, contribuicao) <= 1903.98:
        return base_de_calculo(salario, dependentes, contribuicao)*0 - 0
    elif 1903.99 <= base_de_calculo(salario, dependentes, contribuicao) <= 2826.65:
        return base_de_calculo(salario, dependentes, contribuicao)*0.075 - 142.80
    elif 2826.66 <= base_de_calculo(salario, dependentes, contribuicao) <= 3751.05:
        return base_de_calculo(salario, dependentes, contribuicao)*0.15 - 354.80
    elif 3751.06 <= base_de_calculo(salario, dependentes, contribuicao) <= 4664.68:
        return base_de_calculo(salario, dependentes, contribuicao)*0.225 - 636.13
    elif base_de_calculo(salario, dependentes, contribuicao) > 4664.68:
        return base_de_calculo(salario, dependentes, contribuicao)*0.275 - 869.36
print('O seu imposto de renda é R$ {}'.format(irrf(base_de_calculo)))