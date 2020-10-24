deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + saldo * (taxa / 100)
    print ("Saldo do mês {0} é de R${1:.2f}".format(mes, saldo))
    mes += 1
print ("R${0:.2f}".format(saldo-deposito))