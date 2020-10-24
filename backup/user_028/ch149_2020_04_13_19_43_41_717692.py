salario=float(input('Qual seu salário bruto?'))
dependentes=int(input('Quantos são os dependentes?'))
if salario<=1903.99:
    INSS=salario*0.075
elif salario <= 2089.60:
    INSS=salario*0.09
elif salario <=3134.40:
    INSS=salario*0.12
elif salario <= 6101.06:
    INSS=salario*0.14
else:
    INSS=671.12

bdc=salario-INSS- dependentes*189.59

if bdc <=1903.98:
    aliq=0
    deducao=0
elif bdc <=2826.65:
    aliq=bdc*0.075
    deducao=142.80
elif bdc <=3751.05:
    aliq=bdc*0.15
    deducao=354.80
elif bdc <= 4664.68:
    aliq=bdc*0.225
    deducao=636.13
else:
    aliq=bdc*0.275
    deducao=869.36
IRRF=bdc*aliq-deducao
print(IRRF)
    