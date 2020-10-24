salario_bruto=float(input('Qual é seu salário bruto? '))
while salario_bruto<0:
    salario_bruto=float(input('Valor inválido. Digite novamente: '))

dependentes=int(input('Você tem quantos dependentes? '))
while dependentes<0:
    dependentes=float(input('Valor inválido. Digite novamente: '))
    
if 0<salario_bruto<=1045:
    aliquota=0.075
    INSS=salario_bruto*aliquota
elif 1045.01<=salario_bruto<=2089.60:
    aliquota=0.09
    INSS=salario_bruto*aliquota
elif 2089.61<=salario_bruto<=3134.40:
    aliquota=0.12
    INSS=salario_bruto*aliquota
elif 3134.41<=salario_bruto<=6101.06:
    aliquota=0.14
    INSS=salario_bruto*aliquota
else:    
    INSS=671.12

if INSS+dependentes*189.59>salario_bruto:
    base_de_calculo=0
else:
    base_de_calculo=salario_bruto-INSS-dependentes*189.59

if 0<=base_de_calculo<=1903.98:
    aliquota2=0
    deducao=0
elif 1903.99<=base_de_calculo<=2826.65:
    aliquota2=0.075
    deducao=142.80
elif 2826.66<=base_de_calculo<=3751.05:
    aliquota2=0.15
    deducao=354.80
elif 3751.06<=base_de_calculo<=4664.68:
    aliquota2=0.225
    deducao=636.13
else:
    aliquota2=0.275
    deducao=869.36

IRRF=base_de_calculo*aliquota2-deducao

print(IRRF)
print(0)