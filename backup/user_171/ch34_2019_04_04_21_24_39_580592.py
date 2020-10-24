dp = float(input("Depósito inicial: "))
ti = float(input("Taxa de juros (Ex.: 3 para 3%): "))
m = 1
tot = dp
while m <= 24:
    tot += (tot * (ti / 100))
    print ("Saldo do mês {0} é de R${0:.2f}".format(m, tot))
    m+=1
print ("O ganho obtido com os juros foi de R${0:.2f}".format(tot-dp))