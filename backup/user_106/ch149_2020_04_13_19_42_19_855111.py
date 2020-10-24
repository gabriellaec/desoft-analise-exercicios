salario_bruto=float(input('Qual é seu salário bruto? '))
dependentes=int(input('Você tem quantos dependentes? '))

if salario_bruto<=1045:
    aliquota=0.075
elif 1045.01<=salario_bruto<=2089.60:
    aliquota=0.09
elif 2089.61<=salario_bruto<=3134.40:
    aliquota=0.12
elif 3134.41<=salario_bruto<=6101.06:
    aliquota=0.14
else:    
    INSS=671.12
if not INSS=671.12:
    INSS=salario_bruto*aliquota
    
base_de_calculo=salario_bruto-INSS-dependentes*189.59

if base_de_calculo<=1903.98:
    aliquota2=0
    deducao=0
if 1903.99<=base_de_calculo<=2826.65:
    aliquota2=0.075
    deducao=142.80
if 2826.66<=base_de_calculo<=3751.05:
    aliquota2=0.15
    deducao=354.80
if 3751.06<=base_de_calculo<=4664.68:
    aliquota2=0.225
    deducao=636.13
else:
    aliquota2=0.275
    deducao=869.36

IRRF=base_de_calculo*aliquota2-deducao

print(IRRF)