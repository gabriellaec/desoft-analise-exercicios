inicial = float(input())
taxa = float(input())

saldo = inicial

for mes in range(1, 25):

    saldo += saldo * (taxa / 100)
    print ('%.2f' % saldo)

print ('%.2f' % (saldo - inicial))