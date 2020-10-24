salario_bruto = float(input('qual o seu salario: '))
n_dependentes = float(input('quantos dependentes voce tem? '))
contri_INSS = 0
aliquota = 0 
deducao = 0

if salario_bruto <= 1045:
    contri_INSS = (salario_bruto/100)*7.5
elif salario_bruto <= 2089.60:
    contri_INSS = (salario_bruto/100)*9
elif salario_bruto <= 3134.40:
    contri_INSS = (salario_bruto/100)*12
elif salario_bruto <= 6101.06:
    contri_INSS = (salario_bruto/100)*14
else:
    contri_INSS = 671.12

base_de_calculo = salario_bruto - contri_INSS - (n_dependentes*189.59)



if base_de_calculo <= 1903.98:
    aliquota = 0 
    deducao = 0
elif base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.80   
elif base_de_calculo <=  3751.05:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36

IRRF = (base_de_calculo*aliquota) - deducao


print(base_de_calculo)
print(aliquota)
print(contri_INSS)
print(deducao)

print('o seu Imposto de Renda Retido na Fonte (IRRF), a ser pago é de {0:.2f}'.format(IRRF))
