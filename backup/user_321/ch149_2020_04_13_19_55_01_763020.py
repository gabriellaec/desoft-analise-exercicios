sb = float(input('Salário bruto: '))
nd = int(input('Número de dependentes '))
if sb <= 1045:
    INSS = sb*0.075
elif sb <= 2089.60:
    INSS = sb*0.09
elif sb <= 3134.40:
    INSS = sb*0.12
elif sb <= 6101.06:
    INSS = sb*0.14
else:
    INSS = 671.12
    
bc = sb - INSS - (nd*189.59)

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