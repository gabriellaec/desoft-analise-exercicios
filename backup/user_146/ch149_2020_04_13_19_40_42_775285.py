'''Esse código serve para calcular o Imposto de Renda Retido na Fonte (IRRF) de uma pessoa,
ele pergunta o valor do salário bruto desta pessoa, assim como a quantidade de dependentes
que ela possui.
Na sequencia, dependendo do valor informado do salário, calcula-se a sua contribuição ao
INSS.
Em seguida, o programa calcula a base de calculo para o IRRF e entao, calcula-se o valor
do IRRF
'''
salario_bruto = float(input('Qual o seu salário? '))
dependentes = int(input('Quntos dependentes você possui? '))
if salario_bruto <=1045:
    contribuicao_INSS = salario_bruto *0.075
if salario_bruto >= 1045.01 and salario_bruto <=2089.60:
    contribuicao_INSS = salario_bruto *0.09
if salario_bruto >= 2089.61 and salario_bruto <= 3134.40:
    contribuicao_INSS = salario_bruto*0.12
if salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
    contribuicao_INSS = salario_bruto*0.14
if salario_bruto > 6101.06:
    contribuicao_INSS = 671.12

base_calculo = salario_bruto - contribuicao_INSS - (dependentes*189.59)
if base_calculo <=1903.98:
    aliquota = 0
    deducao = 0
if base_calculo >= 1903.99 and base_calculo <=2826.65:
    aliquota = 0.075
    deducao = 142.8
if base_calculo >= 2826.66 and base_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.8
if base_calculo >= 3751.06 and base_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
if base_calculo > 4664.68:
    aliquota = 0.275
    deducao = 869.36

IRRF = base_calculo *aliquota - deducao
print(IRRF)
    
