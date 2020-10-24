salario = float(input())
dp = int(input())
inss = 0 

if salario <= 1045:
    inss = 0.075*salario
elif salario >= 1045.01 and salario <= 2089.6:
    inss = 0.09*salrio
elif salario >= 2089.61 and salario <= 3134.4:
    inss = 0.12*salario
elif salario >= 3134.41 and salario <= 6101.06:
    inss = 0.14*salario 
else:
    inss = 671.12

base = salario - inss - dp*189.59

if base <= 1903.98:
    irrf = base*0 - 0 
elif base >= 1903.99 and base <= 2826.65:
    irrf = base*0.075  - 142.80
elif base >= 2826.66 and base <= 3751.05:
    irrf = base*0.15 - 354.80
elif base >= 3751.06 and base <= 4664.68:
    irrf = base*0.225 - 636.13
elif base > 4664.68:
    irrf = base*0.275 - 869.36

print(irrf)

