s = float(input('Qual o seu salário bruto? '))
d = float(input('Qual o número de dependentes? '))

if s <= 1045:
    c = 0.075*s
elif s >= 1045.01 and s <= 2089.6:
    c = 0.09*s
elif s >= 2089.61 and s <= 3134.4:
    c = 0.12*s
elif s >= 3134.41 and s <= 6101.06:
    c = 0.14*s
else:
    c = 671.12

bc = s - c - d*189.59

if bc <= 1903.98:
    a = 0
    d = 0
elif bc >= 1903.99 and bc <= 2826.65:
    a = 0.075
    d = 142.8
elif bc >= 2826.66 and  bc <= 3751.05:
    a = 0.15
    d = 354.8
elif bc >= 3751.06 and bc <= 4664.68:
    a = 0.225
    d = 636.13
else:
    a = 0.275
    d = 869.36

ir = bc*a - d

print('O imposto de renda é {0}'.format(ir))