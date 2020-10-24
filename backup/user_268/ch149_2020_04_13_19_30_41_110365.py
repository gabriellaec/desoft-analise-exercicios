salario = float(input("salario"))
dependent = int(input("dependentes"))

INSS = 0
BDC = 0
IRFF = 0

if salario <= 1045.00:
    INSS = salario * 0.075
    
elif 1045.01 <= salario >= 2089.60:
    INSS = salario * 0.09
    
elif 2089.61 <= salario >= 3134.40	:
    INSS = salario * 0.12
    
elif 3134.41 <= salario >= 6101.06	:
    INSS = salario * 0.14
    
elif salario > 6101.06:
    INSS = 671.12
    
BDC = salario - INSS - (dependent * 189.59)

if BDC <= 1903.98:
    ali = 0
    deduc = 0
elif 1903.99 <= BDC <= 2826.65:
    ali = BDC * 0.075
    deduc = 142.80
elif 2826.66 <= BDC <= 3751.05:
    ali = BDC * 0.15
    deduc = 354.80
elif 3751.06 <= BDC <= 4664.68:
    ali = BDC * 0.225
    deduc = 636.13
else:
    ali = BDC * 0.275
    deduc = 869.36
    
IRFF = ali - deduc

print(IRFF)