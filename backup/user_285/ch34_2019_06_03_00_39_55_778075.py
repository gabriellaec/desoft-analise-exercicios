depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
mês = 0
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))
    mês = mês + 1
print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo-depósito))