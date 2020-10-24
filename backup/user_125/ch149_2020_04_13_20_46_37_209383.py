salario = float(input('Qual seu salário '))
dependentes=int(input('Qual seu número de dependentes? '))
if salario_bruto <= 1045.00:
    aliquota = 0.075
elif salario_bruto > 1045.00 and salario_bruto <= 2089.60:
    aliquota = 0.09
elif salario_bruto > 2089.60 and salario_bruto <= 3134.40:
    aliquota = 0.12
else:
    aliquota = 0.14
    contribuicao = salario_bruto*aliquota
else:
    INSS = 671.12
    
base_de_calculo = salario_bruto - contribuicao - dependentes*189.59


if base_de_calculo <= 1903.98:
    aliquota2 = 0
    deducao = 0
elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
    aliquota2 = 0.075
    deducao = 142.80
elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
    aliquota2 = 0.15
    deducao = 354.80
elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
    aliquota2 = 0.225
    deducao = 636.13
else:
    aliquota2 = 0.275
    deducao = 869.36
 
irrf = base_de_calculo*aliquota2 - deducao
print (irrf)