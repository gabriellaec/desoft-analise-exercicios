salario=float(input('Qual o salario bruto? '))
dependentes=int(input('Quantos dependentes? '))
if salario<=1045.00:
    b=salario*0.075
elif 1045.01<salario<2089.60:
    b=salario*0.09
elif 2089.61<=salario<=3134.40:
    b=salario*0.12
elif 3134.41<=salario<=6101.06:
    b=salario*0.14
else:
    b=671.12

base=salario-b-(dependentes*189.59)


if base<=1903.98:
    deducao=0
    aliquota=0
elif 1903.99<=base<=2826.65:
    deducao=142.80
    aliquota=0.075
elif 2826.66<=base<=3751.05:
    deducao=354.80
    aliquota=0.15
elif 3751.06<=base<=4664.68:
    deducao=636.13
    aliquota=0.225
elif base>4664.80:
    deducao=869.36
    aliquota=0.275

irrf=(base*aliquota)-deducao
print (irrf)

    