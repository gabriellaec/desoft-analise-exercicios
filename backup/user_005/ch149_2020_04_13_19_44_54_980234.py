sal_bruto = float(input('qual é o seu salario brutou?:'))
dependentes = int(input('qual o numero de dependentes?:'))
if sal_bruto < 6101.06:
    if sal_bruto <= 1045.00:
        aliq = 0.075
    elif sal_bruto > 1045.00 and sal_bruto <= 2089.60:
        aliq = 0.09
    elif sal_bruto > 2089.60 and sal_bruto <= 3134.40:
        aliq = 0.12
    else:
        aliq = 0.14
    INSS = sal_bruto * aliq
else:
    INSS = 671.12

base_calculo = sal_bruto - INSS - dependentes*189.59

if base_calculo <= 1903.98:
    aliq2 = 0 
    deducao = 0
elif base_calculo >= 1903.99 and base_calculo <= 2826.65:
    aliq2 = 0.075
    deducao = 142.80
elif base_calculo >= 2826.66 and base_calculo <= 3751.05:
    aliq2 = 0.15
    deducap = 354.80
elif base_calculo >= 4664.68:
    aliq2= 0.275
    deducao = 869.36
else:
    aliq2 = 0.225
    deducao = 636.13
IRRF = base_calculo - aliq2 - deducao