sb = float(input('Qual é o seu salário  bruto? '))
nd = int(input('Qual o número de dependentes? '))
a = 0
if sb <= 1045:
    a = 0.075
    INSS = sb*a
if 1045 < sb <= 2089.60:
    a = 0.09
    INSS = sb*a
if 2089.60 < sb <= 3134.40:
    a = 0.12
    INSS = sb*a
if 3134.40 < sb <= 6101.06:
    a = 0.14
    INSS = sb*a
if sb > 6101.06:
    INSS = 671.12
    
bc = sb - INSS - nd*189.59

if bc <= 1903.98:
    al = 0
    ded = 0
elif 1903.98 < bc <= 2826.85:
    al = 0.075
    ded = 142.80
elif 2826.85 < bc <= 3751.05:
    al = 0.15
    ded = 354.80
elif 3751.05 < bc <= 4664.68:
    al = 0.225
    ded = 63.13
elif bc > 4664.68:
    al = 0.275
    ded = 869.36
IRRF = bc*al - ded
print (IRRF)