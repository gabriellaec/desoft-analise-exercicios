salario = float(input('Qual seu salário '))
dependentes=int(input('Qual seu número de dependentes? '))

if salario <=1045.00:
    aliquota=0.075
elif 1045.00<=salario<=2089.60:
    aliquota=0.09
elif 2069.61<=salario<=3134.40:
    aliquota=0.12
elif 3134.41<=salario<=6101.60:
    aliquota=0.14
else:
    contribuicao=671,12
contribuicao=salario*aliquota

base_de_calculo=salario-contribuicao-dependentes*189,59

if base_de_calculo<=1903.98:
    aliquota_2=0
    deducao=0
elif 1903.99<=base_de_calculo<=2826.65:
    aliquota_2=0.075
    deducao=142.80
elif 2826.66<=base_de_calculo<=3751.05:
    aliquota_2=0.15
    deducao:354.80
elif 3751.06<=base_de_calculo<=4664.68:
    aliquota_2=0.225
    deducao=636.13
else:
    aliquota_2=0,275
    deducao=869.13
irff= base_de_calculo*aliquota_2-deducao
print(irff)