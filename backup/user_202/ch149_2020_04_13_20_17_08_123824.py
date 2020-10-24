sb = float(input('Qual o seu salário bruto?: '))
nd = int(input('Qual o numero de dependentes?: '))
INSS = 0
if sb <= 1045.00:
    INSS = 0.075*sb
elif sb >= 1045.00 and sb <= 2089.60:
    INSS = 0.09*sb
elif sb >= 2089.61 and sb <= 3134.40:
    INSS = 0.12*sb
elif sb >= 3134.41 and sb <= 6101.06:
    INSS = 0.14*sb
else:
    INSS = 671.12
base = sb-INSS-(nd*189.59)
aliquota = 0
deducao = 0
if base <= 1903.98:
    aliquota = 0
    deducao = 0
elif base >= 1903.99 and base <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif base >= 2826.66 and base <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
elif base >= 3751.06 and base <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36
IRRF = base*aliquota-deducao
print(IRRF)