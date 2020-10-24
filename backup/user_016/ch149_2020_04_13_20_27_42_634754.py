s = float(input('Qual o salário bruto? '))
d = int(input('Qual o número de dependentes? '))
if s <= 1045:
    c = s*0.075
elif 1045.01 <= s <= 2089.60:
    c = s*0.09
elif 2089.61 <= s <= 3134.40:
    c = s*0.12
elif 3134.41 <= s <= 6101.06:
    c = s*0.14
else:
    c = 671.12

base = s - c - (d*189.59)
if base <= 1903.98:
    IRRF = 0
elif 1903.99 <= base <= 2826.65:
    IRRF = (base*0.075) - 142.80
elif 2826.66 <= base <= 3751.05:
    IRRF = (base*0.15) - 354.80
elif 3751.06 <= base <= 4664.68:
    IRRF = (base*0.225) - 636.13
else:
    IRRF = (base*0.275) - 869.36
print(IRRF)