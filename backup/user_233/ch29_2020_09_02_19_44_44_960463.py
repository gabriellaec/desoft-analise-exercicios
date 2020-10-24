inicial = float(input())
taxa = float(input())

print(taxa)

saldo = inicial

for mes in range(1, 25):

    saldo += saldo * taxa
    print ('%.2f' % saldo)

print ('%.2f' % (saldo - inicial))