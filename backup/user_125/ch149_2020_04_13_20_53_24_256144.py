salario = float(input('Qual seu salário '))
dependentes=int(input('Qual seu número de dependentes? '))
contribuicao = salario*aliquota
if salario <= 1045.00:
    aliquota = 0.075
elif  1045.00<salario  <= 2089.60:
    aliquota = 0.09
elif 2089.60<= salario <= 3134.40:
    aliquota = 0.12
elif 3134.41<=salario<=6101.06:
    aliquota = 0.14
else:
    contribuicao = 671.12
return contribuicao
base_de_calculo = salario - contribuicao - dependentes*189.59

if base_de_calculo <= 1903.98:
    aliquota2 = 0
    deducao = 0
elif 1903.99<=base_de_calculo<=2826.65:
    aliquota2 = 0.075
    deducao = 142.80
elif 2826.66<=base_de_calculo<=3751.05:
    aliquota2 = 0.15
    deducao = 354.80
elif 3751.06<=base_de_calculo<=4664.06:
    aliquota2 = 0.225
    deducao = 636.13
else:
    aliquota2 = 0.275
    deducao = 869.36
 
irrf = base_de_calculo*aliquota2 - deducao
print (irrf)