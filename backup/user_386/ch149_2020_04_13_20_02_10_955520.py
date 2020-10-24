salario=float(input('salario? :'))
dep=float(input('dependentes?: '))

if salario <= 1045:
    INSS = 0.075*salario
if salario > 1045 and salario <= 2089.6:
    INSS = 0.09*salario
if salario > 2089.6 and salario <= 3134.4:
    INSS = 0.12*salario
if salario > 3134.4 and salario<= 6101.06:
    INSS = 0.14*salario
if salario > 6101.06:
    INSS = 671.12
final = salario - INSS - (dep*189.59)
if final <= 1903.98:
    alíquota = 0
    dedução = 0
if final > 1903.98 and final <= 2826.65:
    alíquota = 0.075
    dedução = 142.8
if final > 2826.65 and final <= 3751.05:
    alíquota = 0.15
    dedução = 354.8
if final > 3751.05 and final <= 4664.68:
    alíquota = 0.225
    dedução = 636.13
if final > 4664.68:
    alíquota = 0.275
    dedução = 869.36

IRRF = calc * alíquota - dedução
print(IRRF)