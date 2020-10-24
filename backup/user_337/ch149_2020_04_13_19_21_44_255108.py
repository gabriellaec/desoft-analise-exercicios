salario = float(input('Qual o seu salário bruto? '))
dependentes = int(input('Qual o número de dependentes do usuário? '))
if salario <= 1045:
    contribuicao = salario*0.075
if salario >= 1045.01 and salario <= 2089.60:
    contribuicao = salario*0.09
if salario >=2089.61 and salario <=3134.40:
    contribuicao = salario*0.12
if salario >= 3134.41 and salario <= 6101.06:
    contribuicao = salario*0.14
if salario > 6101.06:
    contribuicao = salario + 617.12

base_de_calculo = salario - contribuicao - dependentes

if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
if base_de_calculo>= 1903.99 and base_de_calculo<=2826.65:
    aliquota = 0.075
    deducao = 142.90
if base_de_calculo>=2826.66 and base_de_calculo <= 3751.05:
    aliquota=0.15
    deducao = 354.80
if base_de_calculo>=3751.06 and base_de_calculo<=4664.68:
    aliquota = 0.225
    deducao = 636.13
if base_de_calculo>4664.68:
    aliquota = 0.275
    deducao = 869.36

IRRF = base_de_calculo*aliquota - deducao
print(IRRF)