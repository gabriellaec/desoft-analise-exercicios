sal=float(input('salario? :'))
dep=float(input('dependentes?: '))

if sal <= 1045:
    INSS = 0.075*sal
if sal > 1045 and sal <= 2089.6:
    INSS = 0.09*sal
if sal > 2089.6 and sal <= 3134.4:
    INSS = 0.12*sal
if sal > 3134.4 and sal<= 6101.06:
    INSS = 0.14*sal
if sal > 6101.06:
    INSS = 671.12
    
calc = sal - INSS - (dep*189.59)


if calc <= 1903.98:
    ali = 0
    ded = 0
if calc > 1903.98 and calc <= 2826.65:
    ali = 0.075
    ded = 142.8
if calc > 2826.65 and calc <= 3751.05:
    ali = 0.15
    ded = 354.8
if calc > 3751.05 and calc <= 4664.68:
    ali = 0.225
    ded = 636.13
if calc > 4664.68:
    ali = 0.275
    ded = 869.36
    
IRRF = calc*ali - ded
print(IRRF)
