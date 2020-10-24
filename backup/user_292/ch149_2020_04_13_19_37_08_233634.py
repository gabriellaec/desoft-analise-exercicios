a = float(input('Qual é o seu salario bruto? '))
b = int(input('Tem quantos dependentes'))
if a <= 1045:
    p = 0.075*a
elif 1045.01 <= a <= 2089.6:
    p = 0.09*a
elif 2089.61 <= a <= 3134.40:
    p = 0.12*a
elif 3134.41 <= a <= 6101.06:
    p = 0.14*a
elif a > 6101.09:
    p = 671.12*a
base = a-p-b*189.59
if base <= 1903.98:
    x = 0
    y = 0
if 1903.99 <= base <= 2826.65:
    x = 0.075 
    y = 142.8
if 2826.66 <= base <= 3751.05:
    x = 0.15
    y = 345.8
if 3751.06 <= base <= 4664.68:
    x = 0.225
    y = 636.13
if base > 4664.68:
    x = 0.275
    y = 869.36
IRRF = base * x - y
print(IRRF)