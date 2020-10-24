y = 1
tx = float(input('tx:'))
pi = float(input('poupança inicial:'))
saldo = 0

mes = 1
while mes <= 24:
    saldo = pi * (1 + tx) ** y
    mes += 1
    y += 1
    print('{0:.2f}'.format(saldo))

print('{0:.2f}'.format(saldo - pi))
    