salario = float(input('Qual o seu salário? '))
depen = int(input('Quantos dependentes voce tem? '))
if salario < 1045.01:
    inss = salario*0.075
if salario in range(1045,2089.59):
    inss = salario*0.09
if salario in range(2089.61,3134.39):
    inss = salario*0.12
if salario in range(3134.4,6101.06):
    inss = salario*0.14
if salario > 6101.06:
    inss = 671.12

base = salario - inss - depen*189.59

if base <= 1903.98:
    irrf = 0
if base in range(1903.99,2826.65):
    irrf = base * 0.075 - 142.8
if base in range(2826.66,3751.05):
    irrf = base * 0.15 - 354.9
if base in range(3751.06,4664.68):
    irrf = base * 0.225 - 636.13
if base > 4664.68:
    irrf = base * 0.275 - 869.36
print(irrf)