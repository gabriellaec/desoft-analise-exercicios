inicial = float(input())
taxa = float(input())

saldo = incial

for mes in range(1, 25):

    saldo += saldo * (taxa / 100)
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))

print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo - inicial))