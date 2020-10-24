sb = int(input('Salário bruto: '))
nd = int(input('Números de dependentes: '))
a = 0
if sb <= 1045:
    a = 7.5
    INSS = sb*a
elif 1045 < sb <= 2089.60:
    a = 9
    INSS = sb*a
elif 2089.60 < sb <= 3134.40:
    a = 12
    INSS = sb*a
elif 3134.40 < sb <= 6101.06:
    a = 14
    INSS = sb*a
elif sb > 6101.06:
    INSS = 671.12
    
bc = sb - INSS - nd*189.59

if bc <= 1903.98:
    al = 0
    ded = 0
elif 1903.98 < bc <= 2826.85:
    al = 7.5
    ded = 142.80
elif 2826.85 < bc <= 3751.05:
    al = 15
    ded = 354.80
elif 3751.05 < bc <= 4664.68:
    al = 22.5
    ded = 636,13
elif bc > 4664.68:
    al = 27.5
    ded = 869.36
IRRF = bc*al - ded
print (IRRF)