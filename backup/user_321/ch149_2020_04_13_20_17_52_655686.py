sb = float(input('Salário bruto:'))
nd = (input("Número de dependentes:"))
if nd == '':
    nd = 0
else:
    nd = int(nd)
    
    
if sb <= 1045.00:
    INSS = sb*0.075
elif sb <= 2089.60:
    INSS = sb*0.09
elif sb <= 3134.40:
    INSS = sb*0.12
elif sb <= 6101.06:
    INSS = sb*0.14
else:
    INSS = 671.12
    
print(INSS)
print (nd)
bc = sb - INSS -(nd*189.59)
print (bc)

if bc <= 1903.98:
    al = 0
    ded = 0
elif bc <= 2826.85:
    al = 0.075
    ded = 142.80
elif bc <= 3751.05:
    al = 0.15
    ded = 354.80
elif bc <= 4664.68:
    al = 0.225
    ded = 636.13
else:
    al = 0.275
    ded = 869.36
IRRF = (bc*al) - ded
print (IRRF)