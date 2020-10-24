depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))
    mês = mês + 1
print ("O ganho obtido com os juros foi de R${0}.2f.".format(saldo-depósito))