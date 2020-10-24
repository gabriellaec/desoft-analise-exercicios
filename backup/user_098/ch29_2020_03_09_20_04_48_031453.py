deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
mês = 1
saldo = deposito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))
    mês = mês + 1
print ("R$%8.2f." % (saldo-deposito))