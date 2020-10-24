x = input('velocidade?')
v = float(x)
n = (v - 80) * 5

if v > 80:
    print('você foi multado em R$%.2f' % n)
else:
    print('Não foi multado')