depósito=float(input("Depósito incial: "))
taxa=float(input("Taxa: "))
mes=1

while mes<=24:
   depósito=depósito+(depósito*(taxa))
   print("Saldo do mes{0} é de {1:.2f}".format(mes,depósito)
   mes +=1
print ("O ganho obtido com os juros foi de {0:.2f}".format(depósito)