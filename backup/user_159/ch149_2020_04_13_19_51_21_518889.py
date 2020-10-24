s = float(input('Salario bruto:'))
d = float(input('Quantos dependentes:'))
inss = 0
if s <= 1045:
    inss = 0.075*s
elif s > 1045 and s <= 2089.6:
    inss = 0.09*s
elif s > 2089.6 and s <= 3134.4:
    inss = 0.12*s
elif s > 3134.4 and s <= 6101.06:
    inss = 0.14*s
else:
    inss = 671.12

bc = s - inss - d * 189.59

if bc <= 1903.98:
    ali = 0
    dedu = 0
elif bc > 1903.98 and bc <= 2826.65:
    ali = 0.075
    dedu = 142.8
elif bc > 2826.65 and bc <= 3751.05:
    ali = 0.15
    dedu = 354.8
elif bc > 3751.05 and bc <= 4664.68:
    ali = 0.225
    dedu = 636.13
else:
    ali = 27.5
    dedu = 869.36

irff = bc * ali - dedu

print(irff)