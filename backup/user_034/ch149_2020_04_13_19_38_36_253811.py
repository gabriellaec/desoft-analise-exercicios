a = float(input("Qual seu salario bruto?:"))
b = float(input("Voce tem quantos dependentes?:"))
if a <= 1045.00:
    INSS = a * 0.075
elif a <= 2089.60:
    INSS = a * 0.09
elif a <= 3134.40:
    INSS = a * 0.12
elif a <= 6101.06:
    INSS = a * 0.14
else:
    INSS = 671.12

base_de_calculo = a - INSS - b * 189.59

if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.80 
elif base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
elif base_de_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36
    
IRRF = base_de_calculo * aliquota - deducao
print(IRRF)