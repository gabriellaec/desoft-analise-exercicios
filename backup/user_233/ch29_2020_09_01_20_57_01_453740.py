inicial = float(input())
taxa = float(input())

saldo = inicial

for mes in range(1, 25):

    saldo += saldo * (taxa / 100)
    print ("Saldo do mês %d é de R$%.2f." % (mes, saldo))

print ("O ganho obtido com os juros foi de R$%.2f." % (saldo - inicial))