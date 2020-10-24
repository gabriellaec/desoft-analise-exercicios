salario = float(input('Qual seu salário'))
dependentes=int(input('Qual seu número de dependentes?'))
aliquota=0
if salario <=1045.00:
    aliquota=0.075
elif 1045.00<=salario<=2089.60:
    aliquota=0.09
elif 2069.61<=salario<=3134.40:
    aliquota=0.12
elif 3134.41<=salario<=6101.60:
    aliquota=0.14
else:
    valorfixo=671,12
contribuicao=salario*aliquota
float(base_de_calculo)=salario-contribuicao-dependentes*189,59
aliquota_2=0
deducao=0
if a<=1903.98:
    aliquota_2=0
    deducao=0
elif 1903.99<=a<=2826.65:
    aliquota_2=0.075
    deducao=142.80
elif 2826.66<=a<=3751.05:
    aliquota_2=0.15
    deducao:354.80
elif 3751.06<=a<=4664.68:
    aliquota_2=0.225
    deducao=636.13
else:
    aliquota_2=0,275
    deducao=869.13
irff= base_de_calculo*aliquota_2-deducao
print(irff)