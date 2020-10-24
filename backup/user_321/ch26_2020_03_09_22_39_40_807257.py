import math
v = float(input('Qual o valor da casa:'))
s = float(input('Qual o salário:'))
a = int(input('Quantos anos:'))

p = v/(a*12)

if (p>s*0.3):
    return 'Empréstimo não aprovado'
else:
    return 'Empréstimo aprovado'