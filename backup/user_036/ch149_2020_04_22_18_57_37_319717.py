salario = float(input('Qual o seu salÃ¡rio? '))
depen = int(input('Quantos dependentes voce tem? '))
if salario < 1045.01:
    inss = salario*0.075
if salario > 1045 and salario < 2089.6:
    inss = salario*0.09
if salario > 2089.6 and salario < 3134.4:
    inss = salario*0.12
if salario > 3134.39 and salario < 6101.07:
    inss = salario*0.14
if salario > 6101.06:
    inss = 671.12

base = salario - inss - depen*189.59

if base <= 1903.98:
    irrf = 0
if base > 1903.98 and base < 2826.66:
    irrf = base * 0.075 - 142.8
if base > 2826.65 and base < 3751.06:
    irrf = base * 0.15 - 354.9
if base > 3751.05 and base < 4664.69:
    irrf = base * 0.225 - 636.13
if base > 4664.68:
    irrf = base * 0.275 - 869.36
print(irrf)