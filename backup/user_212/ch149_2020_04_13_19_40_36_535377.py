salario=float(input('Qual o seu salário?'))
dependentes=int(input('Qual o numero de dependentes?'))

contribuicao=0
base_calculo=0
ali=0
ded=0
IRRF=0


if salario <= 1045.00:
    contribuicao= salario*(0.075)
if salario>=1045.01 and salario<=2089.60:
    contribuicao=salario*0.09
if salario>=2089.61 and salario<=3134.40:
    contribuicao=salario*0.12
if salario>=3134.41 and salario<=6101.06:
    contribuicao=salario*0.14
else:
    contribuicao=671.12
    

base_calculo= salario-contribuicao- (dependentes*189.59)

if base_calculo <= 1903.98:
    ali=0
    ded=0
if base_calculo>= 1903.99 and base_calculo<=2826.65:
    ali=0.075
    ded=142.80
if base_calculo>=2826.66 and base_calculo<=3751.05:
    ali=0.15
    ded=354.80
if base_calculo>=3751.06 and base_calculo<=4664.68:
    ali=0.225
    ded=636.13
else:
    ali=0.275
    ded=869.36



IRRF= (base_calculo*ali) - ded

print (IRRF)