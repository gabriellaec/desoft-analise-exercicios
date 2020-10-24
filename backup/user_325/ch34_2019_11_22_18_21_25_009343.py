depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print ("Saldo do mês {0} é de R${1}".format (mês, saldo))
    mês = mês + 1
print ("O ganho obtido com os juros foi de R${1}".format (saldo-depósito))

    