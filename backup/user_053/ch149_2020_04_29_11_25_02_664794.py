salario_bruto = float(input('Digite o valor de seu salário bruto: R$ '))
dependentes = int(input('Digite o número de dependentes: '))

# Calcula base de cálculo
if salario_bruto <= 1045:
    contribuicao_inss = salario_bruto*0.075
    base_calculo = salario_bruto - contribuicao_inss - dependentes*189.59
elif salario_bruto >= 1045.01 and salario_bruto <= 2089.6:
    contribuicao_inss = salario_bruto*0.09
    base_calculo = salario_bruto - contribuicao_inss - dependentes*189.59
elif salario_bruto >= 2089.61 and salario_bruto <= 3134.4:
    contribuicao_inss = salario_bruto*0.12
    base_calculo = salario_bruto - contribuicao_inss - dependentes*189.59
elif salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
    contribuicao_inss = salario_bruto*0.14
    base_calculo = salario_bruto - contribuicao_inss - dependentes*189.59
else:
    contribuicao_inss = 671.12
    base_calculo = salario_bruto - contribuicao_inss - dependentes*189.59

# Cálculo de alíquota e dedução
if base_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif base_calculo >= 1903.99 and base_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.8
elif base_calculo >= 2826.66 and base_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.8
elif base_calculo >= 3751.06 and base_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36

# Calcula IRRF simplificado
irrf = base_calculo*aliquota - deducao
print('O valor do seu IRRF simplificado é de R$ {0}'.format(irrf))